from flask import Flask, render_template, Blueprint
from seMgmtApp import app
from flask_pymongo import pymongo
from seMgmtApp.config import Config

main = Blueprint("main", __name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

