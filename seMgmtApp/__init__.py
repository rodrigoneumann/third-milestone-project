import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

# Routes
from seMgmtApp.main.routes import main
from seMgmtApp.properties.routes import properties
app.register_blueprint(main)
app.register_blueprint(properties)