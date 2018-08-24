from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Ho!"

@app.route("/user/<username>")
def welcome_user(username):
    return "Welcome: %s" %username
