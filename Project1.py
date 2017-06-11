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


@app.route('/allbooks', methods=["POST","GET"])
def allbooks():
    if request.method == 'POST':
        result = request.form
        data = DbClass().getdata()
        #titel = request.form[0][0]('inputTitel')
        print(result)
        # print(titel)
        return render_template("allbooks.html", result=result,data=data)
    else:
        data = DbClass().getdata()
        return render_template('allbooks.html',data=data)


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/rentedbooks')
def rentedbooks():
    return render_template('rentedbooks.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",3000))

    app.run(host='0.0.0.0', port=port, debug=True)
