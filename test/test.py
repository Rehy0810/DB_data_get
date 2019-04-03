import urllib2
import os
import csv
import json
import random
import dicttoxml

from flask import render_template, Flask,jsonify,make_response, Response
'''https://github.com/newnewcorder/flask-chartjs-demo'''
os.environ['no_proxy']='*'

app = Flask(__name__)

def wpjson():
    r=urllib2.urlopen('http://192.168.10.1/test.json')
    data=json.load(r)

    for radek in data['data']:
        print radek

    return data

@app.route('/json')
def jsex():
    return render_template("xxxx.jinja2",data=wpjson())

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port = port)
