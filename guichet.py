#!/usr/bin/python3.8
from flask import Flask, json, request, Response
import random

api = Flask(__name__)

@api.route('/hello', methods=['GET'])
def hello():
    return "Hello World\n"

if __name__ == '__main__':
   api.run(host='0.0.0.0', port=8081)
