from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
from seMgmtApp.helpers import users_collection

profile = Blueprint("profile", __name__)

@profile.route("/view_profile", methods=["GET", "POST"])
def view_profile():

    if session.get('username'):
        
        agent = session['username']
        agent_details = users_collection.find({ "username": agent })
        
        return render_template("view_profile.html", agent_details=agent_details)

    else:
        flash("You must be logged in to view this page.")
        return redirect(url_for('reg_login.login'))
