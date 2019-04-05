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
            print("invalid query string ")
            return False

        if column_found and condition_found and sematic_mean == 'Logical_operator ':
            logicalObject.append(conditional[i])
            logObject['Logical'] = conditional[i]
            # conditions.append(logObject)
            return validate_conditional(conditional[i+1:], conditions, logicalObject)

        ''' duplicate logical operator  '''
        if sematic_mean == 'Logical_operator ':
            print("invalid query string ")
            return False

        if i == len(conditional) - 1 and column_found and condition_found:
            invalid = False
            print("valid query found ")
            return True


    print("invalid query string ")
    return False

def create_condisional(conditions,logicalObject):
    Query = ""

    for i in range(len(conditions)):

        if( i == len(conditions) -1):
            pass
        else:
            conObject = conditions[i]
            logObject = logicalObject[i]

            columnsqlsyntax,column = conObject['column']
            valuesqlsyntax,value = conObject['value']
            operatorsqlsyntax,operator = conObject['operator']

            Query +=  sqlmapper[columnsqlsyntax] + " " +  sqlmapper[operatorsqlsyntax] + " "+  valuesqlsyntax + " "+ logicalObject

    print(Query)

