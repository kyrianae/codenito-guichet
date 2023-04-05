#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random
import os
import requests

app = Flask("guichet")
pizzaiolo="http://127.0.0.1:8082"

if "PIZZAIOLO" in os.environ:
    pizzaiolo=os.environ["PIZZAIOLO"]
    
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World\n"

@app.route('/pizza', methods=['GET'])
def pizza():
    print ("Guichet\tpizza asked")
    x = requests.get(pizzaiolo+"/make_pizza")
    
    return x.text+"\nGuichet\tJob Done\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
