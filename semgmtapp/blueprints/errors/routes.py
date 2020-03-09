from flask import render_template, Blueprint, session

# Blueprint
errors = Blueprint("errors", __name__)


# 404 Error page


@errors.route("/<path:path>")
def path_error(path):
    return render_template("error.html"), 404
