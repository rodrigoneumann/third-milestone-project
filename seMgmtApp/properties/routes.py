from flask import Flask, Blueprint, render_template, url_for
from seMgmtApp import app
from flask_pymongo import pymongo
from seMgmtApp.config import Config

properties = Blueprint("properties", __name__)

@properties.route("/add_property", methods=["GET", "POST"])
def add_property():
    return render_template("add_property.html")

@properties.route("/edit_property", methods=["GET", "POST"])
def edit_property():
    return render_template("edit_property.html")