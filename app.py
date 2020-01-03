from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<name>")
def index(name):
    return '<h1>Hello, {}!</h1>'.format(name)
 