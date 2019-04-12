import mysql.connector

def get_connection(user, password,host,database):
    connection = mysql.connector.connect(user=user, password=password,
                                  host=host,
                                  database=database)
    return connection


def close_connection(connection):
    return connection.close()




