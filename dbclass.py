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

    def getdata(self):
        q = "select boek.Titel, boek.ISBN, boek.AantalBlz, auteurs.Auteur,categories.Categorie FROM boek JOIN auteurs ON boek.AuteurID=auteurs.AuteurID JOIN categories ON boek.CategorieID=categories.CategorieID;"
        self.__cursor.execute(q)
        data = self.__cursor.fetchall()
        self.__cursor.close()
        print(data)
        return data

    def adddata(self):
        q = ""
        self.__cursor.execute(q)
        add = self.__cursor.fetchall()
        self.__cursor.close()
        print(add)
        return add




