from flask import Flask

# app name
app = Flask(__name__)

# routes

@app.route('/')
def hello_world():
	return 'Hello, World!'