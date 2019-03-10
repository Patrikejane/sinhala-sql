import codecs
import nltk
import nltk.tag, nltk.data
import re
from sklearn.externals import joblib

from Normalizer import Normaliser
from queryGenarator import create_Query



strLine = " සිසුන්ගේ ලකුණු දෙන්න"

# strLine = "සිසුන් දෙන්න"


tagger = joblib.load('posTagger.pkl')
sqlmapper = joblib.load('sqlMapper.pkl')


def tokernizing_clean(text):
    tokens = nltk.word_tokenize(text)

    regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
    tokens = [regex.sub('', w) for w in tokens]

    return tokens


tokeniezed =tokernizing_clean(strLine)
print("tokenized sentence : ", tokeniezed)

normalied_tokens = list(map(Normaliser ,tokeniezed))
print("normalized tokens : ", normalied_tokens )

tagger_list = tagger.tag(normalied_tokens)
print("pos tagged tokens : ", tagger_list)

commands = []
tableNames = []
attributeName = []


for i in tagger_list:
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

print(commands,tableNames,attributeName)

sql_query = create_Query(commands,tableNames,attributeName)

print("Genarated Sql Query : ",sql_query)




