import mysql.connector


# def get_connection(user, password,host,database):
#     connection = mysql.connector.connect(user=user, password=password,
#                                   host=host,
#                                   database=database)
#     return connection
#
#
# def close_connection(connection):
#     return connection.close()


class DbConnector:

    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def get_connection(self):
        connection = mysql.connector.connect(user=self.user, password=self.password,
                                             host=self.host,
                                             database=self.database)
        return connection

    def close_connection(self, connection):
        return connection.close()
