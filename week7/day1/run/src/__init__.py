#!/usr/bin/env python3

from flask import Flask,request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def f():
    if request.method == 'GET':
        return '<a href="DEAF">Welcome to my web app</a>'
    elif request.method == 'POST':
	    pass
    else:
	    print('\n Error: bad HTTP method\n')

@app.route('/<message>', methods=["GET","POST"])
def f1(message):
    if request.method == 'GET':
        if message == message.upper():
            return "I can hear you"
        return "I can\'t hear you" 
       # x = message
       # print(x)
       # return x
    elif request.method == 'POST':
	    pass
    else:
        print('\n Error: bad HTTP method\n')



if __name__=='__main__':
 app.run(port=8000, debug=True)


