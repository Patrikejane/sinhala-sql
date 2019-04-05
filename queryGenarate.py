import codecs
import nltk
import nltk.tag, nltk.data
import re
from sklearn.externals import joblib

from Normalizer import Normaliser
from queryGenarator import create_Query,validate_conditional,create_condisional

boundryTokens = ["සමාන", "වන", "පමණක්", "වැඩි", "වඩා", "අඩු","ක්"]
stopwords = ['ට']

# strLine = " සිසුන්ගේ ලකුණු දෙන්න"

# strLine = "සිසුන්ගේ නම දෙන්න ලකුණු 75 ක් ලබාගත්"
# strLine = "ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සිසුන්ගේ නම දෙන්න"
# strLine = "සිසුන්ගේ නම කුමක්ද ලකුණු 75 ට වැඩි"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සමාන සමාන සමාන"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස වයස 22 ට සමාන"
strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 සමාන"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සමාන සමාන සහ වයස 22 ට සමාන"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ වයස 22 ට සමාන සහ"
# strLine = " සිසුන්ගේ නම දෙන්න ලකුණු 75 ට සමාන සහ සහ වයස 22 ට සමාන"

tagger = joblib.load('posTagger.pkl')
sqlmapper = joblib.load('sqlMapper.pkl')


def tokernizing_clean(text):
    tokens = nltk.word_tokenize(text)

    # regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    # tokens = [regex.sub('', w) for w in tokens]

    return tokens


tokeniezed =tokernizing_clean(strLine)
print("tokenized sentence : ", tokeniezed)

normalied_tokens_stop = list(map(Normaliser ,tokeniezed))
print("normalied_tokens_stop tokens : ", normalied_tokens_stop )

#remove stop words
normalied_tokens = [item for item in normalied_tokens_stop if item not in stopwords]
print("normalied_tokens tokens : ", normalied_tokens )

tagger_list = tagger.tag(normalied_tokens)
print("pos tagged tokens : ", tagger_list)

tagedDict = h = {v:k for k,v in tagger_list}

tagger_list_norm = []
for i in tagger_list:
    sqlsyntax, sematic_mean = i
    if sematic_mean != "unnecessary_word":
        tagger_list_norm.append(i)
    else:
        normalied_tokens.remove(sqlsyntax)


# tagger_list_norm = [v for k,v in tagedDict if k != 'unnecessary_word']


# print("tagged list norm  : ",tagger_list_norm)
# print("tagged dict : ",tagedDict)

boundryIndexs = {}
for i in boundryTokens:
    reversednorm = normalied_tokens[::-1]
    boundryIndexs[i] = len(reversednorm) - 1 -reversednorm.index(i) if i in normalied_tokens else -1

# print("bround index : " , boundryIndexs)

boundryIndex =  max(boundryIndexs.values())
# print("bround index : " , boundryIndex)

commandIndex = normalied_tokens.index(tagedDict.get('command'))
# tableIndex = normalied_tokens.index(tagedDict.get('Table'))


mainQuery = ''
conditionalQuery = ''
if boundryIndex < commandIndex :
    conditionalQuery = tagger_list_norm[:boundryIndex + 1]
    mainQuery = tagger_list_norm[boundryIndex+1:]
    # print("conditional part befor main")

else:
    mainQuery = tagger_list_norm[:commandIndex + 1]
    conditionalQuery = tagger_list_norm[commandIndex + 1::]
    # print("conditional part after main ")

print("main query :",mainQuery)
print("conditional part : ", conditionalQuery)


commands = []
tableNames = []
attributeName = []


for i in mainQuery:
    sqlsyntax, sematic_mean  = i
    if sematic_mean != "unnecessary_word":
        sqlSyntax = sqlmapper[sqlsyntax]
        if sematic_mean == "Table" :
            tableNames.append(sqlSyntax)

        elif sematic_mean == "column":
            attributeName.append(sqlSyntax)

        elif sematic_mean == "command":
            commands.append(sqlSyntax)

    else:
        print("unnecessary word")

# print(commands,tableNames,attributeName)

conditions = []
logicalObject = []

sql_query_main_Query = create_Query(commands,tableNames,attributeName)
conditional_validation = validate_conditional(conditionalQuery,conditions,logicalObject)



if conditional_validation:
    print( 'Conditional true string' )
    sql_conditinal_query = create_condisional(conditions, logicalObject)
else:
    print('invalid string')
    # sql_conditinal_query = create_condisional(conditions, logicalObject)



print("Genarated Sql Query : ",sql_query_main_Query )
print( "conditional Query  : " , conditional_validation )

print("conditions : ", conditions)
print("logic : ",logicalObject)


# print(type(1))
# print("11".isdigit() )
# # print(int("a"))


