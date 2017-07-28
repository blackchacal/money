from flask import request

from .app import app, db
from .models import *

# handle database connection on request
@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

# API routes
@app.route('/')
def hello_world():
	return 'Hello, World!'