#!/usr/bin/env python3

from flask import Flask, render_template, session, requests, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def frontpage():
    return render_template('index.html')

@app.route('/phone/iphone-<int:version>', methods=['GET'])
def find_iphone(version):
    versions = [3,4,5,'5s',6,'6s',7,'7s', 8, 'x', 'xr']
    if versions in versions:
        print('works')
        return render_template('iphone.html')
    

if __name__ == '__main__':
    app.run(debug=True)
