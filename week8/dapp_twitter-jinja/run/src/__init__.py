#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session, flash
import model
import re
import dateutil.parser
import calendar


app = Flask(__name__)

app.secret_key = b'#5566778'

@app.route('/', methods=['GET'])
def send_to_login():
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'GET':
        print(session)
        if 'username' in session:
            return redirect('/message_board')
        return render_template('login.html')
    else:
        try:
            username = request.form['username']
            password = request.form['password']
            user_object = model.set_user_object(username)
        except:
            flash("Invalid Login")
            return redirect('/login')
        if user_object.check_password(user_object.pass_hash, password):
            session['username'] = username
            flash(f'User {username} successfully logged in!')
            return redirect('/login')
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
        flash('User Account Successfully Created')
        return redirect('/login')



@app.route('/message_board', methods=['GET', 'POST'])
def message_board():
    if request.method == 'GET':
        if 'username' in session:
            user_id = session['username']
            print(user_id)
            content = model.read_all_tweets(user_id)
            content_len = len(model.read_all_tweets(user_id))
            print(content)
            return render_template('message-board.html', content = content, content_len = content_len)
    if request.method == 'POST':
        if 'username' in session:
            user_id = session['username']
            content = request.form['content']
            print(content)
            try:
                model.create_tweet(user_id,content)
            except:
                ValueError
            flash('Successful Tweet')               
            return redirect('/message_board')
            

@app.route('/logout', methods=['GET'])
def log_out():
    session.clear()
    flash(f'User logged out')
    return redirect('/login')




if __name__ == '__main__':
    app.run(debug=True)