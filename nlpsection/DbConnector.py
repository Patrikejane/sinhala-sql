import mysql.connector


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
