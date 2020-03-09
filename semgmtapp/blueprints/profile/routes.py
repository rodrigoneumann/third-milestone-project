from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    session,
    flash,
)
from bson.objectid import ObjectId
from semgmtapp.helpers import users_collection, properties_collection

profile = Blueprint("profile", __name__)


@profile.route("/view_profile", methods=["GET", "POST"])
def view_profile():
    """
    READ - View Profile Page
    Check if there is a session active and them display the user profile page
    if not, return a message for the user and return to the index.
    """
    if session.get("username"):

        agent = session["username"]
        agent_details = users_collection.find({"username": agent})

        return render_template(
            "view_profile.html", agent=agent, agent_details=agent_details
        )

    flash("You must be logged in to view this page.")
    return redirect(url_for("main.index"))


@profile.route("/view_profile/<username>/change_photo", methods=["GET", "POST"])
def change_photo(username):
    """
    UPDATE - Change an user profile Photo
    First check if there is an active session and then
    if the user is the owner of the profile and then then send the new link to
    the user's photo in database.
    Then a confirmation message is displayed.
    If there is no active session, an error message will be displayed and
    forwarded to the index.
    """
    # Check if there is a session
    if session:
        # Check if session user is the account owner
        if session["username"] == username:
            users_collection.update(
                {"username": username},
                {"$set": {"photoUrl": request.form.get("photoUrl")}},
            )
            flash(
                " {} your profile photo was successfully updated.".format(
                    username.capitalize()
                )
            )
            return redirect(url_for("profile.view_profile"))

        flash("You must be the profile owner to update the photo")
        return redirect(url_for("properties.my_ads"))
    # If not logged in, redirect to login page
    flash("You must be logged in to view this page.")
    return redirect(url_for("main.index"))


@profile.route("/view_profile/<username>/delete_account", methods=["GET", "POST"])
def delete_account(username):
    """
    DELETE an user account from the database
    First check if there is an active session,
    and confirms if the user is the owner of the profile link.
    After the modal confirmation the account
    and all ads created by the user will be deleted from the database.
    Session data from that user is cleared from the browser
    and confirmation message is displayed
    """
    # Check if there is a session
    if session:
        # Check if session user is the account owner
        if session["username"] == username:
            # Delete user from Users collection
            users_collection.delete_one({"username": username})

            # Delete all Ads from this Agent
            properties_collection.delete_many({"agent": username.upper()})

            # Clear session data
            session.pop("username", None)

            # Flash Alert with confirmation
            flash("Your account has been successfully deleted.")

            return redirect(url_for("main.index"))
        flash("You must be the account owner to delete this account.")
        return redirect(url_for("properties.my_ads"))
    # If not logged in, redirect to login page
    flash("You must be logged in to view this page.")
    return redirect(url_for("main.index"))


@profile.route("/view_profile/<username>/change_password", methods=["GET", "POST"])
def change_password(username):
    """
    UPDATE - Change an user password
    First check if there is an active session,
    if the user is the owner of the profile and then
    updates the new password for the database.
    Then a confirmation message is displayed.
    If there is no active session,
    an error message will be displayed and forwarded to the index.
    """
    # Check if there is a session
    if session:
        # Check if session user is the account owner
        if session["username"] == username:
            users_collection.update(
                {"username": username},
                {"$set": {"password": request.form.get("password")}},
            )
            flash(
                " {} your password has been updated successfully .".format(
                    username.capitalize()
                )
            )
            return redirect(url_for("profile.view_profile"))
        flash("You must be the account owner to change the password")
        return redirect(url_for("properties.my_ads"))

    # If not logged in, redirect to login page
    flash("You must be logged in to view this page.")
    return redirect(url_for("main.index"))
