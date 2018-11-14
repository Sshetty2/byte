#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'the session needs this'

@app.route('/', methods=['GET'])
def homepage():
    return render_template('homepage.html')

@app.route('/homepage', methods=['GET'])
def homepage_route():
    return render_template('homepage.html')

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method == 'GET':
        return render_template('addition.html')
    else: 
        input_one = int(request.form['input_one'])
        input_two = int(request.form['input_two'])
        total = input_one + input_two
        flash(f'The total is {total}')
        return redirect('/addition')
        
@app.route('/subtraction', methods=['GET', 'POST'])
def subtraction():
    if request.method == 'GET':
        return render_template('subtraction.html')
    else: 
        input_one = int(request.form['input_one'])
        input_two = int(request.form['input_two'])
        total = input_one - input_two
        flash(f'The result is {total}')
        return redirect('/subtraction')
        
@app.route('/division', methods=['GET', 'POST'])
def division():
    if request.method == 'GET':
        return render_template('division.html')
    else: 
        input_one = int(request.form['input_one'])
        input_two = int(request.form['input_two'])
        total = input_one / input_two
        flash(f'The result is {total}')
        return redirect('/division')
        
@app.route('/multiplication', methods=['GET', 'POST'])
def multiplication():
    if request.method == 'GET':
        return render_template('multiplication.html')
    else: 
        input_one = int(request.form['input_one'])
        input_two = int(request.form['input_two'])
        total = input_one * input_two
        flash(f'The result is {total}')
        return redirect('/multiplication')

@app.route('/modulus_division', methods=['GET', 'POST'])
def modulus_division():
    if request.method == 'GET':
        return render_template('modulus_division.html')
    else: 
        input_one = int(request.form['input_one'])
        input_two = int(request.form['input_two'])
        total = input_one % input_two
        flash(f'The result is {total}')
        return redirect('/modulus_division')


if __name__=='__main__':
    app.debug = True
    app.run()
