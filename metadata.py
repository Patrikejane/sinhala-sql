from nlpsection.sqlexcetor import get_connection, close_connection

user = 'root'
password = 'sunimalroot'
host = '127.0.0.1'
database = 'nlpDb'


connection = get_connection(user,password,host,database)

cursor = connection.cursor()


cursor.execute("SHOW TABLES;")

table_list = []

for i in cursor:
    table_list.append((i[0], 'Table'))


# print(table_list)

DB_dict = {}
for i in table_list:
    cursor.execute("DESCRIBE " + i[0])

    colums_list = []
    for j in cursor:
        colums_list.append((j[0], 'column'))
    # print(colums_list)
    DB_dict[(i[0],'Table')] = colums_list

print(DB_dict)

