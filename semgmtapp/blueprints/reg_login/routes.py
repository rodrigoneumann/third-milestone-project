from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session,
    flash,
)
from semgmtapp.helpers import users_collection

# Blueprint
reg_login = Blueprint("reg_login", __name__)


@reg_login.route("/register", methods=["POST", "GET"])
def register():

    # Check if there is an active session, if not, continue
    if not session:
        # User registration - check user/password
        if request.method == "POST":
            users = users_collection
            is_user = users.find_one({"username": request.form["username"].lower()})
            if not is_user:
                users.insert_one(
                    {
                        "username": request.form["username"].lower(),
                        "password": request.form["password"],
                    }
                )
                session["username"] = request.form["username"].lower()
                # Flash Alert with confirmation
                flash("Your account was created successfully.")
                return redirect(url_for("main.index"))
            else:
                flash(
                    "Sorry, '{}' is already in use, please choose another username.".format(
                        request.form["username"].upper()
                    )
                )
            return redirect(url_for("reg_login.register"))

        return render_template("register.html")
    # Session Alert
    flash(
        "You cannot register another account while logged in, Please log out and try again"
    )
    return redirect(url_for("main.index"))


@reg_login.route("/login", methods=["POST", "GET"])
def login():

    # Check if there is an active session, if not, continue
    if not session:
        if request.method == "POST":
            users = users_collection
            is_user = users.find_one({"username": request.form["username"].lower()})

            if is_user:
                if request.form["password"] == is_user["password"]:
                    session["username"] = request.form["username"]
                    flash("You are logged in.")
                    return redirect(url_for("properties.my_ads"))

                flash("Incorrect username or password. Please try again.")
                return redirect(url_for("reg_login.login"))

            flash(
                "Username {} is not yet registered.".format(
                    request.form["username"].upper()
                )
            )
        return render_template("login.html")

    # Session Alert
    flash(
        "You cannot access the login page while logged in, Please log out and try again"
    )
    return redirect(url_for("main.index"))


@reg_login.route("/logout")
def logout():

    # Check if there is an active session
    if session:
        # Clear session data
        session.pop("username", None)
        flash("You have successfully logged out. See you soon.")
        return redirect(url_for("main.index"))

    # Session not active alert
    flash("You are already logged out of the platform")
    return redirect(url_for("main.index"))

