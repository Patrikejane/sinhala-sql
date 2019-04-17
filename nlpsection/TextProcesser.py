import codecs
import nltk
import nltk.tag, nltk.data
import re
from sklearn.externals import joblib

from nlpsection.Normalizer import Normaliser
# from nlpsection.queryGenarator import validate_main, validate_conditional, create_condisional, create_main_query,\
#     genarate_boundry_command ,tokernizing_clean, separate_main_conditional,main_query_tokens,concat_query

from nlpsection.QueryGenerator import QueryGenerator
from nlpsection.stopwords import get_stopwordlist


'''

Class Implementation TextProcesser

'''


class TextProcesser:

    def __init__(self, Text):
        self.strLine = Text
        self.stopwords = ['ට', 'වල'] + get_stopwordlist()
        self.tagger = joblib.load('nlpsection/posTagger.pkl')
        # self.sqlmapper = joblib.load('nlpsection/sqlMapper.pkl')

    def genarate_query(self):

        normalizer = Normaliser("/Users/sskmal/Documents/Nlpk/NlpkPhaseOne/nlpsection/sinhala_dictionary.txt")
        textProcessorUtil = QueryGenerator()

        GENARATED_SQL_QUERY = ""

        print("Sinhala String Query : ", self.strLine)

        tokeniezed = textProcessorUtil.tokernizing_clean(self.strLine)
        print("tokenized sentence : ", tokeniezed)

        # with stop words
        normalied_tokens_stop = list(map(normalizer.normalise, tokeniezed))
        print("normalied_tokens with stop words : ", normalied_tokens_stop)

        # remove stop words
        normalied_tokens = [item for item in normalied_tokens_stop if item not in self.stopwords]
        print("normalied_tokens removed stop words : ", normalied_tokens)

        # tag the stop word removed string
        tagger_list = self.tagger.tag(normalied_tokens)
        print("pos tagged tokens : ", tagger_list)

        tagedDict = h = {v: k for k, v in tagger_list}

        # remove unnecessary words
        tagger_list_norm = []
        for i in tagger_list:
            sqlsyntax, sematic_mean = i
            if sematic_mean != "unnecessary_word":
                tagger_list_norm.append(i)
            else:
                normalied_tokens.remove(sqlsyntax)

        # tagger_list_norm = [v for k,v in tagedDict if k != 'unnecessary_word']

        # boundry index and command index
        boundryIndex, commandIndex = textProcessorUtil.genarate_boundry_command(normalied_tokens, tagedDict)

        # separate main query and conditional query
        mainQuery, conditionalQuery = textProcessorUtil.separate_main_conditional(boundryIndex, commandIndex,
                                                                                  tagger_list_norm)

        print("main query :", mainQuery)
        print("conditional part : ", conditionalQuery)

        # torkanize main query
        commands, tableNames, attributeName, functions = textProcessorUtil.main_query_tokens(mainQuery)

        # print(commands,tableNames,attributeName)

        conditions = []
        logicalObject = []

        sql_query_main_Query = textProcessorUtil.validate_main(mainQuery, commands, tableNames, attributeName)
        main_query = textProcessorUtil.create_main_query(sql_query_main_Query)
        conditional_validation = textProcessorUtil.validate_conditional(conditionalQuery, conditions, logicalObject)

        GENARATED_SQL_QUERY = main_query[0]
        GENARATED_SQL_FUNCTION = main_query[1]

        GENARATED_SQL_QUERY = textProcessorUtil.concat_query(conditional_validation, conditions, GENARATED_SQL_QUERY,
                                                             logicalObject,
                                                             GENARATED_SQL_FUNCTION)
        # print(GENARATED_SQL_QUERY)

        return GENARATED_SQL_QUERY
