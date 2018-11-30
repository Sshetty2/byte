#!/usr/bin/env python3

from flask import Flask
import connexion
import model

controller = connexion.App(__name__, specification_dir='./')

controller.add_api('swagger.yml')

if __name__ == '__main__':
    controller.run(debug=True)