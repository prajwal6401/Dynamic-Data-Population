from flask import Flask, jsonify, request
import json
import pymysql as p
import pandas as pd

app = Flask(__name__)


@app.route('/getstockdata', methods=['GET','POST'])
def getstockdata():
    dbc = p.connect(host = 'localhost', user = 'root', password = '9482589562', db = 'abc')
    mycursor = dbc.cursor()
    q1 = 'select * from stockprices;'
    mycursor.execute(q1)
    res = mycursor.fetchall()
    # print(res)
    # count = res[0][0]
    dbc.close()
    return jsonify({'reccount' : res})




@app.route('/getstockdataabc', methods=['GET','POST'])
def getstockdataabc():
    dbc = p.connect(host = 'localhost', user = 'root', password = '9482589562', db = 'abc')
    mycursor = dbc.cursor()
    q1 = 'select * from stockpricesabc;'
    mycursor.execute(q1)
    res = mycursor.fetchall()
    # print(res)
    # count = res[0][0]
    dbc.close()
    return jsonify({'reccount' : res})




if __name__ == '__main__':
    app.run(debug=True)

