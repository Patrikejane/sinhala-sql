from nlpsection.DbConnector import DbConnector

# user = 'root'
# password = 'sunimalroot'
# host = '127.0.0.1'
# database = 'nlpDb'
#
# dbConnector = DbConnector(user, password, host, database)
#
# connection = dbConnector.get_connection()
#
# cursor = connection.cursor()
#
#
# cursor.execute("SHOW TABLES;")
#
# table_list = []
#
# for i in cursor:
#     table_list.append((i[0], 'Table'))
#
#
# # print(table_list)
#
# DB_dict = {}
# for i in table_list:
#     cursor.execute("DESCRIBE " + i[0])
#
#     colums_list = []
#     for j in cursor:
#         colums_list.append((j[0], 'column'))
#     # print(colums_list)
#     DB_dict[(i[0],'Table')] = colums_list
#
# print(DB_dict)

class MetaDataExtractor:

    def __init__(self,user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def getDbConnecton(self):
        dbConnector = DbConnector(self.user, self.password, self.host, self.database)

        connection = dbConnector.get_connection()


        return connection

    def getTables(self):
        table_list = []
        connection = self.getDbConnecton()
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")

        for i in cursor:
            table_list.append((i[0], 'Table'))
        return table_list

    def getDbMetadataDict(self):
        tableList = self.getTables()
        connection = self.getDbConnecton()
        cursor = connection.cursor()
        DB_dict = {}
        for i in tableList:
            cursor.execute("DESCRIBE " + i[0])

            colums_list = []
            for j in cursor:
                colums_list.append((j[0], 'column'))
            # print(colums_list)
            DB_dict[(i[0], 'Table')] = colums_list

        return DB_dict





