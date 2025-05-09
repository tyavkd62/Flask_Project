'''
플라스크에서의 요청 처리
'''
from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f'Requested language: {language}'