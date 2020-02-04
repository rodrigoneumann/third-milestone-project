from flask import render_template, Blueprint

#Blueprint
reg_login = Blueprint("reg_login", __name__)


@reg_login.route("/register")
def register():
    return render_template("register.html")

@reg_login.route("/login")
def login():
    return render_template("login.html")

