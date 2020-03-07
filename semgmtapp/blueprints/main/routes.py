from flask import render_template, Blueprint, redirect, session
from semgmtapp.helpers import properties_collection

# Blueprint
main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():
    """ READ - Home page with 2 carousels - for rent and for sale. """

    # MongoDB Queries for Sale, Rent or All for carousel - show only ads with image
    for_sale = properties_collection.find(
        {"$and": [{"imgUrl": {"$ne": ""}}, {"sale_price": {"$gt": "1"}}]}
    ).limit(4)
    for_rent = properties_collection.find(
        {"$and": [{"imgUrl": {"$ne": ""}}, {"rent_price": {"$gt": "1"}}]}
    ).limit(4)

    return render_template("index.html", for_sale=for_sale, for_rent=for_rent)
