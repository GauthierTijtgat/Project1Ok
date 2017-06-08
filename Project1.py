from flask import Flask
from flask import render_template
import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/allbooks')
def allbooks():
    return render_template('allbooks.html')


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

if __name__ == '__main__':
    #port = int(os.environ.get("PORT",5000))
    #app.run(host='0.0.0.0', port=80, debug=True)
    app.run()