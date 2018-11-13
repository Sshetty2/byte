#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session, flash
import model
import re

app = Flask(__name__)
app.secret_key = 'the session needs this'

@app.route('/', methods=['GET'])
def send_to_login():
    print(session)
    if 'username' in session:    
        return redirect('/homepage')
    else:
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(session)
        if 'username' in session:
            return render_template('login_logged.html')
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        new_user = model.Account(username)
        new_user = new_user.set_from_username()
        print(new_user.pass_hash)
        if new_user.check_password(new_user.pass_hash, password):
            session['username'] = username
            return render_template('login_logged.html')
        else:
            flash("Invalid Login")
            return redirect('/login')

@app.route('/create_account', methods=['GET', 'POST'])
def create_new_account():
    if request.method == 'GET':
        if 'username' in session:
            return render_template('create_account_logged.html')
        return render_template('create_account.html')
    else:
        username = request.form['username']
        password = request.form['password']
        model.Account(username)
        new_user = model.Account(username)
        print(new_user)
        if new_user.check_set_username():
            flash('User Already Exists')
            return redirect('/create_account')
        if len(password) < 8:
            flash('Please enter a password that is at least 8 characters')
            return redirect('/create_account')
        if re.search('[0-9]',password) is None:
            flash('Please enter a password that has at least one digit')
            return redirect('/create_account')
        if re.search('[A-Z]',password) is None:
            print('pass char')
            flash('Please enter a password that with at least one capital letter')
            return redirect('create_account')
        print('no issues')
        hashed_pw = new_user.calculatehash(password)
        print(hashed_pw)
        new_user.pass_hash = hashed_pw
        new_user.balance = 0
        new_user.type = "USER"
        new_user.save()
        session['username'] = username
        session['password'] = password
        return render_template('login.html', message = 'Account Successfully Created')


@app.route('/homepage', methods=['GET'])
def show_homepage():
    return render_template('success.html', username=session['username'])

@app.route('/logout', methods=['GET'])
def log_out():
    print(session)
    session.pop('username', None)
    session.clear()
    print(session)
    return redirect('/login')

# def check_user(username, password):
#     """Usually this would be more complicated database logic, we should take
#     security seriously in actual applications.

#     For now, Username and Password are both "Greg"
#     """
#     if username == 'Greg' and password == 'Greg':
#         return True
#     return False

if __name__=='__main__':
    app.debug = True
    app.run()
