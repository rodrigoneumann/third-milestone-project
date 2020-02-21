from flask import render_template, Blueprint, redirect, session
from seMgmtApp.helpers import (properties_collection)

#Blueprint
main = Blueprint("main", __name__)

@main.route("/", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def index():

    # MongoDB Queries for Sale, Rent or All for carousel
    for_sale = properties_collection.find({"$and": [{'imgUrl': { "$ne": "" }}, {"sale_price": {"$gt": "1"}}]}).limit(5)
    for_rent = properties_collection.find({"$and": [{'imgUrl': { "$ne": "" }}, {"rent_price": {"$gt": "1"}}]}).limit(5)

    return render_template("index.html",
                           for_sale=for_sale,
                           for_rent=for_rent)

