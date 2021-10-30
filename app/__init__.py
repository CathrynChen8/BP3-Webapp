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

from flask import Blueprint, current_app, g, render_template, redirect, request, flash, url_for, session
from flask.cli import with_appcontext

from werkzeug.security import check_password_hash, generate_password_hash

import sqlite3
import click

import random
import string

message_bp = Blueprint('message', __name__, url_prefix='/message')

def get_message_db():
    if 'message_db' not in g:
        g.message_db = sqlite3.connect('message_db.sqlite')


    cmd = """CREATE TABLE IF NOT EXISTS message( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        message TEXT NOT NULL)"""

    cursor = g.message_db.cursor()

    cursor.execute(cmd)

    return g.message_db




def insert_message(request):

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        db = get_message_db()
        error = None

        if not name:
            error = 'Name or handle is required.'
        elif not message:
            error = 'message is required.'

        cursor = db.cursor()

        if error is None:
            cursor.execute(
                'INSERT INTO message (name, message) VALUES (?, ?)',
                (name, message)
            )
            db.commit()

        db.close()

def random_messages(n):
    db = get_message_db()
    cursor = db.cursor()
    #cmd1 = """ SELECT COUNT(*) AS m FROM message"""
    #cmd2 = """SELECT * FROM message LIMIT 1 OFFSET name"""
    cmd = """SELECT * FROM message ORDER BY RANDOM() LIMIT """ + str(n)
   #cmd = """SELECT * from message where rowid = (abs(random()) % (select (select max(rowid) from message)+1))"""
    #cursor.execute(cmd1)
    #cursor.execute(cmd2)
    cursor.execute(cmd)
    result = cursor.fetchall()
    db.close()
    return result


 

@app.route('/submit_message/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    if request.method == "POST":
        insert_message(request)
        return render_template('submit.html')


@app.route('/view/')
def view():
    message = random_messages(5)
    return render_template('view.html', messages = message)
    








