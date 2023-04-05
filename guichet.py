#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random
import os
import requests
import datetime

app = Flask("guichet")
pizzaiolo="http://127.0.0.1:8082"

def str_now():
    return str(datetime.datetime.now())

if "PIZZAIOLO" in os.environ:
    pizzaiolo=os.environ["PIZZAIOLO"]
    
@app.route('/hello', methods=['GET'])
def hello():
    return str_now()+"\t"+"Guicher says: Hello World\n"

@app.route('/pizza', methods=['GET'])
def pizza():
    print (str_now()+"\t"+"Guichet\customer asked pizza")
    url=pizzaiolo+"/make_pizza"
    print (str_now()+"\t"+"Guicher calls: "+url)
    x = requests.get(url)
    print (x.text)
    print (str_now()+"\t"+"Guichet\t\tPizza delivered")
    return x.text+"\n"+str_now()+"\t"+"Guichet\t\tPizza delivered\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
