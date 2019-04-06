from sklearn.externals import joblib

sqlmapper = joblib.load('sqlMapper.pkl')

def create_Query(OperationsList,listOfTableName,listOfAttributes):

    if len(OperationsList) == 0 or len(listOfTableName) == 0:
        print("invalid input")
        return -1

    Query = ""

    Query += OperationsList[0] + " "

    if len(listOfAttributes) == 0 :
        Query += ' * '
    else:
        for i in range(len(listOfAttributes)):
            Query += listOfAttributes[i]
            if i != len(listOfAttributes) -1 :
                Query += ','

    Query += " from "+ listOfTableName[0] + " "

    return Query

def validate_conditional(conditional, conditions,logicalObject):
    if len(conditional) > 0:
        conObject = {}
        logObject = {}

        # for i in conditional:
        #     sqlsyntax, sematic_mean = i
        #     if sematic_mean != "unnecessary_word":
        #         sqlSyntax = sqlmapper[sqlsyntax]
        #         print(sqlSyntax)
        #
        #     else:
        #         print("unnecessary word")

        column_found = False
        condition_found = False

        for i in range(len(conditional)):
            sqlsyntax, sematic_mean = conditional[i]
            if (not column_found) and sematic_mean == 'column':
                conObject['column'] = conditional[i]
                conObject['value'] = conditional[i + 1]
                column_found = True
                continue

            if column_found and ( not condition_found) and sematic_mean == 'Condition _ operator':
                conObject['operator'] = conditional[i]
                conditions.append(conObject)
                condition_found = True
                ''' duplicate Condition operator  '''
            elif condition_found and sematic_mean == 'Condition _ operator':
                # print("invalid query string ")
                return False

            if column_found and condition_found and sematic_mean == 'Logical_operator ':
                logicalObject.append(conditional[i])
                logObject['Logical'] = conditional[i]
                # conditions.append(logObject)
                return validate_conditional(conditional[i+1:], conditions, logicalObject)

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


def create_condisional(conditions,logicalObject):
    Query = ""

    for i in range(len(conditions)):

        conObject = conditions[i]

        columnsqlsyntax, column = conObject['column']
        valuesqlsyntax, value = conObject['value']
        operatorsqlsyntax, operator = conObject['operator']

        if( i == len(conditions) -1):

            Query += " " + sqlmapper[columnsqlsyntax] + " " + sqlmapper[operatorsqlsyntax] + " " + valuesqlsyntax

        else:

            logicalsyntax,logical = logicalObject[i]

            Query +=  sqlmapper[columnsqlsyntax] + " " +  sqlmapper[operatorsqlsyntax] + " "+  valuesqlsyntax + " "+  sqlmapper[logicalsyntax]

    return Query

