# to run this website and watch for changes: 
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sklearn as sk
import matplotlib.pyplot as plt
import numpy as np
import pickle

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import io
import base64


# Create web app, run with flask run
# (set "FLASK_ENV" variable to "development" first!!!)

app = Flask(__name__)

# Create main page (fancy)

@app.route('/')

# def main():
#     return render_template("main.html")

# comment out the below to focus on just the fundamentals

# after running
# $ export FLASK_ENV=development; flask run
# site will be available at 
# http://localhost:5000

def main():
    return render_template('main_better.html')

@app.route('/submit_message/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            return render_template('submit.html', name=request.form['name'], message=request.form['message'])
        except:
            return render_template('submit.html')


@app.route('/view/', methods=['POST', 'GET'])
def view():
    return render_template('view.html')


from flask import Blueprint, current_app, g, render_template, redirect, request, flash, url_for, session
from flask.cli import with_appcontext

from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
import click

import random
import string

message_bp = Blueprint('message', __name__, url_prefix='/message')

def get_message_db():
    if 'db' not in g:
        g.message_db = sqlite3.connect('message_db.sqlite')

    return g.message_db


    








