from flask import Flask
from flask import render_template, request
import os
import RPi.GPIO as GPIO
import time
import _json
import json
app = Flask(__name__)
import mysql.connector
from dbclass import DbClass
GPIO.setmode(GPIO.BCM)
led = 26
DK = 6
buz = 19
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buz, GPIO.OUT)
GPIO.setup(DK, GPIO.IN)
GPIO.output(led, GPIO.LOW)
GPIO.output(buz, GPIO.LOW)


listcategorien = ["Educatie", "Technologie", "Actie", "Reizen", "Fantasy"]



@app.route('/')
def home():
    return render_template('index.html')
    # def homebutton():
    #     while True:
    #
    #         if DK == GPIO.LOW:
    #             return render_template('addbook.html')
    #         else: break




@app.route('/allbooks', methods=["POST","GET"])
def allbooks():
        data = DbClass().getdata()
        return render_template('allbooks.html',data=data)




@app.route('/addedbook',methods=['GET', 'POST'])
def addedbook():
    nData = DbClass().adddata()
    nAuteur = DbClass().addauteur()
    GPIO.output(led, GPIO.HIGH)
    GPIO.output(buz, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led, GPIO.LOW)
    GPIO.output(buz, GPIO.LOW)
    return render_template('index.html', nData=nData)



@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/rentedbooks')
def rentedbooks():
    return render_template('rentedbooks.html')








if __name__ == '__main__':
    port = int(os.environ.get("PORT",3000))

    app.run(host='0.0.0.0', port=port, debug=True)


