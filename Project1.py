from flask import Flask
from flask import render_template, request
import os
import _json
import json
app = Flask(__name__)
import mysql.connector
from dbclass import DbClass

listcategorien = ["Educatie", "Technologie", "Actie", "Reizen", "Fantasy"]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/allbooks')
def allbooks():
    titel = DbClass().gettitels()
    # isbn = DbClass().getISBN()
    return render_template('allbooks.html',titel=titel)


@app.route('/addbook', methods=["POST", "GET"])
def addbook():
    return render_template('addbook.html')

@app.route('/rentedbooks')
def rentedbooks():
    return render_template('rentedbooks.html')

@app.route('/storage')
def storage():
    _titel = request.form['inputTitel']
    _auteur = request.form['inputAuteur']
    _isbn = request.form['inputISBN']
    _aantalblz = request.form['inputAantalblz']
    _Categorie = request.form['inputCategorie']

    print(_titel)
    if _Categorie and _aantalblz and _auteur and _isbn and _titel:
        if _Categorie not in listcategorien:
            return json.dumps({'html':'<span>Kies de categorie uit: Educatie, Technologie, Actie,      Reizen,Fantasy![Case Sensitive]</span>}'})
        else:
            return json.dumps({'html':'<span>Boek wordt toegevoegd!'})
    return render_template('allbooks.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT",3000))

    app.run(host='0.0.0.0', port=port, debug=True)
