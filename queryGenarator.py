def create_Query(OperationsList,listOfTableName,listOfAttributes):

    if len(OperationsList) == 0 or len(listOfTableName) == 0:
        print("invalid input")
        return -1

    Query = ""

    Query += OperationsList[0] +" "

    if len(listOfAttributes) == 0 :
        Query += ' * '
    else:
        for i in range(len(listOfAttributes)):
            Query += listOfAttributes[i]
            if i != len(listOfAttributes) -1 :
                Query += ','

    Query += " from "+ listOfTableName[0] + " "

    return Query