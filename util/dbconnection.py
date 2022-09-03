import mysql.connector
from mysql.connector import Error

class DatabaseConnect:
    def __init__(self):
        try:
            ALL_KEYS = open('./secrets/secrets.txt', 'r').read().splitlines()
            HOST = ALL_KEYS[0]
            DATABASE = ALL_KEYS[1]
            USER = ALL_KEYS[2]
            PASSWORD = ALL_KEYS[3]
            self.connection = mysql.connector.connect(host=HOST,
                                                database=DATABASE,
                                                user=USER,
                                                password=PASSWORD)
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)

    def disconnect(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            cursor.close()
            self.connection.close()
            print("MySQL connection is closed")