from flask import Flask, render_template
from seMgmtApp import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/add_property")
def add_property():
    return render_template("add_property.html")

@app.route("/edit_property")
def edit_property():
    return render_template("edit_property.html")