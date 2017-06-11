class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "gauthier",
            "passwd": "tresor123",
            "db": "mydb"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def gettitels(self):
        q = "SELECT Titel FROM boek"
        self.__cursor.execute(q)
        titels = self.__cursor.fetchall()
        self.__cursor.close()
        return titels




