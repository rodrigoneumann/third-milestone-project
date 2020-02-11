from flask import Blueprint, render_template, redirect, request, url_for
from seMgmtApp.helpers import (properties_collection, dropdown_properties_type, dropdown_num_beds,
                               dropdown_num_baths, dropdown_districts)

properties = Blueprint("properties", __name__)


@properties.route("/add_property", methods=["GET", "POST"])
def add_property():

    if request.method == "GET":

        type_list = dropdown_properties_type()
        num_beds_list = dropdown_num_beds()
        num_baths_list = dropdown_num_baths()
        districts_list = dropdown_districts()

        return render_template("add_property.html",
                               types=type_list,
                               num_bed=num_beds_list,
                               num_bath=num_baths_list,
                               districts=districts_list)

    if request.method == "POST":
        properties = properties_collection
        properties.insert_one(request.form.to_dict())
        return redirect(url_for('properties.add_property'))


@properties.route("/edit_property", methods=["GET", "POST"])
def edit_property():
    type_list = dropdown_properties_type()
    num_beds_list = dropdown_num_beds()
    num_baths_list = dropdown_num_baths()
    districts_list = dropdown_districts()

    return render_template("edit_property.html",
                           types=type_list,
                           num_bed=num_beds_list,
                           num_bath=num_baths_list,
                           districts=districts_list)

@properties.route("/properties_listing", methods=["GET", "POST"])
def list_properties():
    all = properties_collection.find( { "address": {"$exists":True } } )

    if request.method == "GET":
        sort_by_selector = request.form.get('.sort_by')
    for_sale = properties_collection.find( { "$and": [{"for_sale" : {"$ne": "" }}, {"for_sale" : {"$exists": True }}]})
    for_rent = properties_collection.find( { "address": {"$exists":True } , "for_rent" : {"$ne" : "null" } } )
    return render_template("properties_listing.html",
                           all=all,
                           sort_by_selector=sort_by_selector,
                           for_sale=for_sale,
                           for_rent=for_rent)