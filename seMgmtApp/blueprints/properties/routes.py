from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
import math
from seMgmtApp.helpers import (users_collection, properties_collection, dropdown_properties_type, dropdown_num_beds,
                               dropdown_num_baths, dropdown_districts)


properties = Blueprint("properties", __name__)


@properties.route("/add_property", methods=["GET", "POST"])
def add_property():

    if session.get('username'):
        if request.method == "GET":

            type_list = dropdown_properties_type()
            num_beds_list = dropdown_num_beds()
            num_baths_list = dropdown_num_baths()
            districts_list = dropdown_districts()
            agent = session['username'].upper()

            return render_template("add_property.html",
                                   types=type_list,
                                   num_bed=num_beds_list,
                                   num_bath=num_baths_list,
                                   districts=districts_list,
                                   agent=agent)

        if request.method == "POST":
            properties = properties_collection
            properties.insert_one(request.form.to_dict())

            # After add a new property it's redirected to my_ads page
            return redirect(url_for('properties.my_ads'))
    else:
        flash("You must be logged in to view this page.")
        return redirect(url_for('reg_login.login'))


@properties.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):

    if request.method == "GET":
        type_list = dropdown_properties_type()
        num_beds_list = dropdown_num_beds()
        num_baths_list = dropdown_num_baths()
        districts_list = dropdown_districts()

        property_details = properties_collection.find(
            {"_id": ObjectId(property_id)})
        agent = session['username'].upper()

        return render_template("edit_property.html",
                               property_details=property_details,
                               agent=agent,
                               types=type_list,
                               num_bed=num_beds_list,
                               num_bath=num_baths_list,
                               districts=districts_list)

    if request.method == "POST":

        properties_collection.update_one({"_id": ObjectId(property_id)}, {
                                         '$set': request.form.to_dict()})

        return redirect(url_for('properties.my_ads'))


@properties.route("/delete_property/<property_id>", methods=["GET", "POST"])
def delete_property(property_id):

    properties_collection.delete_one({"_id": ObjectId(property_id)})

    return redirect(url_for('properties.my_ads'))


@properties.route("/my_ads", methods=["GET", "POST"])
def my_ads():

    if session.get('username'):
        # Get the session username and set for the agent variable
        agent = session['username'].upper()

        # value of selection , sale, rent or all in searching dropdown
        sort_by_selector = request.args.get('search2')

        # MongoDB Queries for Sale, Rent or All
        for_sale = properties_collection.find(
            {"$and": [{"agent": agent}, {"sale_price": {"$gt": "1"}}]})
        for_rent = properties_collection.find(
            {"$and": [{"agent": agent}, {"rent_price": {"$gt": "1"}}]})
        all_properties = properties_collection.find({"agent": agent})

            # Sort_by_selector variable is set by dropdown in my_adds.html template
        if sort_by_selector is None or sort_by_selector == "all_properties":
            sort_by_selector = all_properties
            # Pagination properties counter based into sort selector choose
            properties_pagination = all_properties.count()
        if sort_by_selector == "for_rent":
            sort_by_selector = for_rent
            # Pagination properties counter based into sort selector choose
            properties_pagination = for_rent.count()
        if sort_by_selector == "for_sale":
            sort_by_selector = for_sale
            # Pagination properties counter based into sort selector choose
            properties_pagination = for_sale.count()

        # Pagination
        properties_per_page = 6
        current_page = int(request.args.get('current_page', 1))
        num_pages = range(1, int(math.ceil(properties_pagination / properties_per_page)) + 1)
        properties = sort_by_selector.skip((current_page - 1) * properties_per_page).limit(properties_per_page)

        return render_template("my_ads.html", sort_by_selector=sort_by_selector,
                                        properties=properties,
                                        current_page=current_page,
                                        pages=num_pages)

    else:
        flash("You must be logged in to view this page.")
        return redirect(url_for('reg_login.login'))


@properties.route("/properties_list", methods=["GET", "POST"])
def list_properties():

    # value of selection , sale, rent or all in searching dropdown
    sort_by_selector = request.args.get('search')

    # MongoDB Queries for Sale, Rent or All
    for_sale = properties_collection.find({"sale_price": {"$gt": "1"}})
    for_rent = properties_collection.find({"rent_price": {"$gt": "1"}})
    all_properties = properties_collection.find(
        {"$or": [{"sale_price": {"$gt": "1"}}, {"rent_price": {"$gt": "1"}}]})

    # Sort_by_selector variable is set by dropdown in properties_listing.html template

    if sort_by_selector is None or sort_by_selector == "all_properties":
        sort_by_selector = all_properties
        # Pagination properties counter based into sort selector choose
        properties_pagination = all_properties.count()
    if sort_by_selector == "for_rent":
        sort_by_selector = for_rent
        # Pagination properties counter based into sort selector choose
        properties_pagination = for_rent.count()
    if sort_by_selector == "for_sale":
        sort_by_selector = for_sale
        # Pagination properties counter based into sort selector choose
        properties_pagination = for_sale.count()

    # Pagination
    properties_per_page = 6
    current_page = int(request.args.get('current_page', 1))
    num_pages = range(1, int(math.ceil(properties_pagination / properties_per_page)) + 1)
    properties = sort_by_selector.skip((current_page - 1) * properties_per_page).limit(properties_per_page)


    return render_template("properties_list.html",
                           sort_by_selector=sort_by_selector,
                           for_sale=for_sale,
                           for_rent=for_rent,
                           properties=properties,
                           current_page=current_page,
                           pages=num_pages)


@properties.route("/property_details/<property_id>", methods=["GET", "POST"])
def property_details(property_id):

    # checks if there is a user logged in, if yes, the variable agent for checking property is rendered
    if session.get('username'):
        property_details = properties_collection.find(
            {"_id": ObjectId(property_id)})
        agent = session['username'].upper()
        
        return render_template("property.html", property_details=property_details, agent=agent)
    else:
        property_details = properties_collection.find(
            {"_id": ObjectId(property_id)})
        return render_template("property.html", property_details=property_details)

