from flask import render_template, request
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
        q = "select boek.Titel, boek.ISBN, boek.AantalBlz, auteurs.Auteur,categories.Categorie FROM  boek JOIN auteurs ON boek.AuteurID=auteurs.AuteurID JOIN categories ON boek.CategorieID=categories.CategorieID;"
        self.__cursor.execute(q)
        data = self.__cursor.fetchall()
        self.__cursor.close()
        print(data)
        return data

    def adddata(self):
        print('Entered')
        nTitel = request.form['inputTitel']
        print(nTitel)
        nISBN = request.form['inputISBN']
        print(nISBN)
        # nCategorie = request.form['inputCategorie']
        nAantalblz = request.form['inputAantalblz']
        print(nAantalblz)
        self.__cursor.execute("""INSERT INTO mydb.boek(Titel,AantalBlz,ISBN) VALUES (%s,%s,%s)""",(nTitel,nAantalblz,nISBN))
        self.__connection.commit()
        print('addedbook')


    def addauteur(self):
        nAuteur = request.form['inputAuteur']
        print(nAuteur)
        print("enteredauteur")
        q = "INSERT INTO mydb.auteurs(Auteur) VALUES ('{auteur}')"
        qcommand = q.format(auteur = nAuteur)
        self.__cursor.execute(qcommand)
        self.__connection.commit()
        self.__connection.close()
        print('addedauter')






