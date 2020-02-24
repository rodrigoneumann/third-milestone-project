from flask import Flask, render_template, request, redirect, url_for, Blueprint, session, flash
from seMgmtApp.helpers import users_collection

# Blueprint
reg_login = Blueprint("reg_login", __name__)


@reg_login.route("/register", methods=['POST', 'GET'])
def register():

    # User registration - check user/password
    if request.method == 'POST':
        users = users_collection
        is_user = users.find_one(
            {"username": request.form['username'].lower()})
        if not is_user:
            users.insert_one({"username": request.form['username'].lower(),
                              "password": request.form['password']})
            session['username'] = request.form['username'].lower()
            return redirect(url_for('main.index'))
        else:
            flash("Sorry, '{}' is already in use, please choose another username.".format(
                request.form['username'].upper()))
        return redirect(url_for('reg_login.register'))

    return render_template('register.html')


@reg_login.route("/login", methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        users = users_collection
        is_user = users.find_one(
        {"username": request.form['username'].lower()})

        if is_user:
            if request.form['password'] == is_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('properties.list_properties'))
            else:
                flash("Incorrect username or password. Please try again.")
                return redirect(url_for('reg_login.login'))
        else:
            flash("Username {} is not yet registered.".format(
                request.form['username'].upper()))
    return render_template('login.html')


@reg_login.route("/logout")
def logout():
    # Clear session data
    session.pop('username', None)
    return redirect(url_for('main.index'))
