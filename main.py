#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random

app = Flask("guichet")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
