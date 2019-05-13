from sklearn.externals import joblib
import nltk
import re


'''
Class Implementation of Text Processer Util functions
'''


class QueryGenerator:

    def __init__(self):
        self.sqlmapper = joblib.load('nlpsection/sqlMapper.pkl')
        self.boundryTokens = ["සමාන", "වන", "පමණක්", "වැඩි", "වඩා", "අඩු", "ක්"]

    def validate_main(self, mainQuery, OperationsList, listOfTableName, listOfAttributes):
        tablename = ''
        columns = []
        command = ''
        functions = ""
        calculation = ''

        table_found = False
        calculation_found = False
        function_found = False
        column_found = False
        command_found = False

        # print(functions, mainQuery)
        ''' new implementation '''
        for i in range(len(mainQuery)):
            sqlsyntax, sematic_mean = mainQuery[i]
            if not table_found and sematic_mean == "Table":
                table_found = True
                tablename += self.sqlmapper[sqlsyntax]

            if table_found and sematic_mean == 'column':
                column_found = True
                columns.append(self.sqlmapper[sqlsyntax])

            if table_found and not command_found and sematic_mean == 'command':
                command += self.sqlmapper[sqlsyntax]

            if not function_found and sematic_mean == 'function':
                functions += self.sqlmapper[sqlsyntax]
                function_found = True
                sq, sem = mainQuery[i - 1]
                if function_found and sem == 'column' and columns.count(self.sqlmapper[sq]) > 0:
                    columns.remove(self.sqlmapper[sq])
                    functions += " " + self.sqlmapper[sq]

            if not calculation_found and sematic_mean == 'calculation':
                calculation_found = True
                calculation += self.sqlmapper[sqlsyntax]

        if len(listOfAttributes) == 0:
            columns.append("*")

        query_dic = {}
        query_dic['table'] = tablename
        query_dic['columns'] = columns
        query_dic['command'] = command
        query_dic['functions'] = functions
        query_dic['calculation'] = calculation

        if len(OperationsList) == 0 or len(listOfTableName) == 0:
            print("invalid input")
            return -1

        # Query = ""
        #
        # Query += OperationsList[0] + " "
        #
        # if len(listOfAttributes) == 0 :
        #     Query += ' * '
        # else:
        #     for i in range(len(listOfAttributes)):
        #         Query += listOfAttributes[i]
        #         if i != len(listOfAttributes) -1 :
        #             Query += ','
        #
        # Query += " from "+ listOfTableName[0] + " "

        return query_dic

    def combineMultipleLogics(self,listConditions):
        newCondition = ''
        for i in listConditions:
            newCondition += i[0]

        newConditionTag = (newCondition, 'Condition _ operator')
        # print('new Condition tag : ', newConditionTag)
        return newConditionTag

    def findCombinedLogics(self,normalise_tokens):
        RETURN_LIST = normalise_tokens
        indexes = []
        for i in range(len(normalise_tokens)):
            sqlsyntax0, sematic_mean0 = normalise_tokens[i]
            if (sematic_mean0 == 'Condition _ operator' and i != len(normalise_tokens) - 1):
                sqlsyntax1, sematic_mean1 = normalise_tokens[i + 1]
                if (sematic_mean1 == 'Logical_operator ' and i + 1 != len(normalise_tokens) - 1):
                    sqlsyntax2, sematic_mean2 = normalise_tokens[i + 2]
                    if sematic_mean2 == 'Condition _ operator':
                        A, B, C = RETURN_LIST[:i], RETURN_LIST[i:i + 2 + 1], RETURN_LIST[i + 2 + 1:]
                        multipleCond = self.combineMultipleLogics(B)

                        indexes.append((i, multipleCond))

        # print(indexes)
        return indexes

    def recreateTagedNormedlist(self,normalise_tokens, indexes):
        newLs = normalise_tokens
        newIndexes = []
        for i in range(len(indexes)):
            index, tag = indexes[i]
            newLs.insert(index + (1 * i), tag)
            newIndexes.append(index + (1 * i))

        # print('new list : ', newLs)

        newtaggedList = []
        for i in range(len(newIndexes)):
            if (i == 0):
                newtaggedList += newLs[:(newIndexes[i] + 1)]
            else:
                newtaggedList += newLs[(newIndexes[i - 1] + 4):(newIndexes[i] + 1)]

        # print('new tagged list : ', newtaggedList)
        return newtaggedList

    def validate_conditional(self, conditional, conditions, logicalobject):
        if len(conditional) > 0:
            conObject = {}
            logObject = {}

            column_found = False
            condition_found = False

            for i in range(len(conditional)):
                sqlsyntax, sematic_mean = conditional[i]
                if (not column_found) and sematic_mean == 'column':
                    conObject['column'] = conditional[i]
                    conObject['value'] = conditional[i + 1]
                    column_found = True
                    continue

                if column_found and (not condition_found) and sematic_mean == 'Condition _ operator':
                    conObject['operator'] = conditional[i]
                    conditions.append(conObject)
                    condition_found = True
                    ''' duplicate Condition operator  '''
                elif condition_found and sematic_mean == 'Condition _ operator':
                    # print("invalid query string ")
                    return False

                if column_found and condition_found and sematic_mean == 'Logical_operator ':
                    logicalobject.append(conditional[i])
                    logObject['Logical'] = conditional[i]
                    # conditions.append(logObject)
                    return self.validate_conditional(conditional[i + 1:], conditions, logicalobject)

                ''' duplicate logical operator  '''
                if sematic_mean == 'Logical_operator ':
                    # print("invalid query string ")
                    return False

                if i == len(conditional) - 1 and column_found and condition_found:
                    invalid = False
                    # print("valid query found ")
                    return True

            # print("invalid query string ")
            return False
        else:
            return True

    def create_condisional(self, conditions, logicalobject):
        Query = ""

        for i in range(len(conditions)):

            conobject = conditions[i]

            columnsqlsyntax, column = conobject['column']
            valuesqlsyntax, value = conobject['value']
            operatorsqlsyntax, operator = conobject['operator']

            if i == len(conditions) - 1:

                Query += " " + self.sqlmapper[columnsqlsyntax] + " " + self.sqlmapper[
                    operatorsqlsyntax] + " " + valuesqlsyntax

            else:

                logicalsyntax, logical = logicalobject[i]

                Query += self.sqlmapper[columnsqlsyntax] + " " + self.sqlmapper[
                    operatorsqlsyntax] + " " + valuesqlsyntax + " " + \
                         self.sqlmapper[logicalsyntax]

        return Query

    def create_main_query(self, main_dict):
        main_query = ''
        functions = ''
        # print(main_dict)
        if len(main_dict['command']) > 0:
            main_query += main_dict['command']

        if len(main_dict['calculation']) > 0:
            main_query += " " + main_dict['calculation'] + '('
            column_list = ','.join(main_dict['columns'])
            main_query += column_list + ')'
        else:
            main_query += " " + ','.join(main_dict['columns'])

        if len(main_dict['table']) > 0:
            main_query += " FROM " + main_dict['table']

        if len(main_dict['functions']) > 0:
            functions += main_dict['functions']
        else:
            functions += ''

        return main_query, functions

    def genarate_boundry_command(self, normalied_tokens, tagedDict):
        boundryIndexs = {}
        for i in self.boundryTokens:
            reversednorm = normalied_tokens[::-1]
            boundryIndexs[i] = len(reversednorm) - 1 - reversednorm.index(i) if i in normalied_tokens else -1

        boundryIndex = max(boundryIndexs.values())
        # print("bround index : " , boundryIndex)

        commandIndex = normalied_tokens.index(tagedDict.get('command'))

        return boundryIndex, commandIndex

    def tokernizing_clean(self, text):
        tokens = nltk.word_tokenize(text)

        # regex = re.compile(u'[^\u0D80-\u0DFF]', re.UNICODE)
        # tokens = [regex.sub('', w) for w in tokens]

        return tokens

    def separate_main_conditional(self, boundryIndex, commandIndex, tagger_list_norm):
        mainQuery = ''
        conditionalQuery = ''
        if boundryIndex < commandIndex:
            conditionalQuery = tagger_list_norm[:boundryIndex + 1]
            mainQuery = tagger_list_norm[boundryIndex + 1:]
            # print("conditional part befor main")

        else:
            mainQuery = tagger_list_norm[:commandIndex + 1]
            conditionalQuery = tagger_list_norm[commandIndex + 1::]
            # print("conditional part after main ")
        return mainQuery, conditionalQuery

    def main_query_tokens(self, mainQuery):
        commands = []
        tableNames = []
        attributeName = []
        functions = []

        for i in mainQuery:
            sqlsyntax, sematic_mean = i
            if sematic_mean != "unnecessary_word":
                sqlSyntax = self.sqlmapper[sqlsyntax]
                if sematic_mean == "Table":
                    tableNames.append(sqlSyntax)

                elif sematic_mean == "column":
                    attributeName.append(sqlSyntax)

                elif sematic_mean == "command":
                    commands.append(sqlSyntax)
                elif sematic_mean == "function":
                    functions.append(sqlSyntax)

            else:
                print("unnecessary word")

        return commands, tableNames, attributeName, functions

    def concat_query(self, conditional_validation, conditions, GENARATED_SQL_QUERY, logicalObject,
                     GENARATED_SQL_FUNCTION):

        if conditional_validation and len(conditions) == 0:
            GENARATED_SQL_QUERY += ""
        elif conditional_validation:
            # print( 'Conditional true string' )
            sql_conditinal_query = self.create_condisional(conditions, logicalObject)

            GENARATED_SQL_QUERY += " WHERE " + sql_conditinal_query
        else:
            GENARATED_SQL_QUERY = "INVALID QUERY"
            # sql_conditinal_query = create_condisional(conditions, logicalObject)

        GENARATED_SQL_QUERY = GENARATED_SQL_QUERY + " " + GENARATED_SQL_FUNCTION
        return GENARATED_SQL_QUERY
