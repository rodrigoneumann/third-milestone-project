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
    """
    CREATE - Register a new user
    First check if there is an active session, if yes
    then an error message is displayed an the user is forwarded do the index.
    if not, after the user submits the desired username and password,
    check if user already exists in the database.
    if user already exists, an "existing user" message will be displayed,
    if it is a new user it will be successfully added to the database.
    And then a confirmation message is displayed.
    """
    # Check if there is an active session, if not, continue
    if session:
        # Session Alert
        flash("You cannot register another account while logged in")
        return redirect(url_for("main.index"))

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
            return redirect(url_for("properties.my_ads"))
        else:
            flash(
                "Sorry, '{}' is already in use, please choose another username.".format(
                    request.form["username"].upper()
                )
            )

    return render_template("register.html")


@reg_login.route("/login", methods=["POST", "GET"])
def login():
    """
    READ - User Login
    First check if there is an active session, if yes
    then an error message is displayed an the user is forwarded to the index.
    if not, after the user submits username and password,
    check if user exists in the database.
    if the user has not been registered yet,
    an "User not registered" message will be displayed, if  user exists,
    check if the password is correct.
    And then a login confirmation message is displayed.
    """
    # Check if there is an active session, if not, continue
    if session:
        # Session Alert
        flash("You cannot access the login page while logged in")
        return redirect(url_for("main.index"))

    if request.method == "POST":
        users = users_collection
        is_user = users.find_one({"username": request.form["username"].lower()})

        if is_user:
            if request.form["password"] == is_user["password"]:
                session["username"] = request.form["username"]
                flash("You are logged in.")
                return redirect(url_for("properties.my_ads"))

            flash("Incorrect Password. Please try again.")

        else:
            flash(
                "Username {} is not yet registered.".format(
                    request.form["username"].upper()
                )
            )
    return render_template("login.html")


@reg_login.route("/logout")
def logout():
    """
    User Logout
    First check if there is an active session, if yes
    then the user session is cleared from the browser and
    the user is forwarded to the index.
    if not, a message 'You are already logged out of the platform' is displayed
    """
    # Check if there is an active session
    if session:
        # Clear session data
        session.pop("username", None)
        flash("You have successfully logged out. See you soon.")
        return redirect(url_for("main.index"))

    # Session not active alert
    flash("You are already logged out of the platform")
    return redirect(url_for("main.index"))
