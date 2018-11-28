#!/usr/bin/env python3

from flask import Flask, request, render_template, url_for
import connexion

from .models import model

controller = connexion.App(__name__, specification_dir='./')

controller.add_api('swagger.yml')

# @controller.route('/', methods=['GET','POST'])
# def frontpage():
#     if request.method == 'GET':
#         message = 'Hello, World'
#         return render_template('index.html', m=message)
#     else: 
#         x = request.form['tweet']
#         print('before context is established')
#         with model.Database() as db:
#             db.cursor.execute('CREATE TABLE users(pk INTEGER PRIMARY KEY AUTOINCREMENT);'.format(x=x))
#             print('after context is used but before its torn down')
#         return render_template('index.html', tweets=[x])

if __name__ == '__main__':
    controller.run(debug=True)