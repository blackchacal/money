import os
from flask import Flask
from peewee import SqliteDatabase

# config data
APP_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(APP_ROOT, 'money.db')

# app instance
app = Flask(__name__)
app.config.from_object(__name__)

# database setup
db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)