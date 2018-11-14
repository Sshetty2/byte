#!/usr/bin/env python3

from flask import Flask, render_template 

supercontroller = Flask(__name__)

@supercontroller.route('/')
def dashboard():
    data = xs
    return render_template('dashboard.html', message = data)


xs = [['a'], ['b'], ['c'], ['d'], ['e']]
