from flask import Blueprint, render_template, redirect, request, url_for, session, flash
from bson.objectid import ObjectId
import math
from semgmtapp.helpers import (
    users_collection,
    properties_collection,
    dropdown_properties_type,
    dropdown_num_beds,
    dropdown_num_baths,
    dropdown_districts,
)


properties = Blueprint("properties", __name__)


@properties.route("/add_property", methods=["GET", "POST"])
def add_property():

    # Check if there is a session
    if session.get("username"):
        if request.method == "GET":

            type_list = dropdown_properties_type()
            num_beds_list = dropdown_num_beds()
            num_baths_list = dropdown_num_baths()
            districts_list = dropdown_districts()
            agent = session["username"].upper()

            return render_template(
                "add_property.html",
                types=type_list,
                num_bed=num_beds_list,
                num_bath=num_baths_list,
                districts=districts_list,
                agent=agent,
            )

        if request.method == "POST":
            properties = properties_collection
            properties.insert_one(request.form.to_dict())

            # After add a new property it's redirected to my_ads page
            # Flash Alert with confirmation
            flash("Your Ad has been successfully added.")
            return redirect(url_for("properties.my_ads"))

    flash("You must be logged in to view this page.")
    return redirect(url_for("reg_login.login"))


@properties.route("/edit_property/<property_id>", methods=["GET", "POST"])
def edit_property(property_id):

    # Check if there is a session
    if session:
        # Check if session user is the ads owner
        property = properties_collection.find_one(
            ObjectId(property_id), {"agent": 1, "_id": 0}
        )
        agent = session["username"].upper()
        if agent == property["agent"]:
            # Request the property information to the base
            if request.method == "GET":
                type_list = dropdown_properties_type()
                num_beds_list = dropdown_num_beds()
                num_baths_list = dropdown_num_baths()
                districts_list = dropdown_districts()

                property_details = properties_collection.find(
                    {"_id": ObjectId(property_id)}
                )
                agent = session["username"].upper()

                return render_template(
                    "edit_property.html",
                    property_details=property_details,
                    agent=agent,
                    types=type_list,
                    num_bed=num_beds_list,
                    num_bath=num_baths_list,
                    districts=districts_list,
                )
            # Send the updated info to the db
            if request.method == "POST":

                properties_collection.update_one(
                    {"_id": ObjectId(property_id)}, {"$set": request.form.to_dict()}
                )
                # Flash Alert with update confirmation
                flash("The property details have been updated successfully.")
                return redirect(
                    url_for("properties.property_details", property_id=property_id)
                )
        # If not owner redirect to my_ads page
        flash("You must be the profile owner to edit that property")
        return redirect(url_for("properties.my_ads"))
    # If not logged in, redirect to login page
    flash("You must be logged in to view this page.")
    return redirect(url_for("reg_login.login"))


@properties.route("/delete_property/<property_id>", methods=["GET", "POST"])
def delete_property(property_id):

    # Check if there is a session
    if session:
        # Check if session user is the ads owner
        property = properties_collection.find_one(
            ObjectId(property_id), {"agent": 1, "_id": 0}
        )
        agent = session["username"].upper()
        if agent == property["agent"]:
            properties_collection.delete_one({"_id": ObjectId(property_id)})
            # Flash Alert with delete confirmation
            flash("The property has been successfully deleted from your list.")
            return redirect(url_for("properties.my_ads"))
        # If not owner redirect to my_ads page
        flash("You must be the profile owner to delete that property")
        return redirect(url_for("properties.my_ads"))
    # If not logged in, redirect to login page
    flash("You must be logged in to view this page.")
    return redirect(url_for("reg_login.login"))


@properties.route("/my_ads", methods=["GET", "POST"])
def my_ads():

    # Only the ads of the logged-in agent will be displayed.
    # All ads on MY_ADS page will have the EDIT and DELETE buttons enabled
    if session.get("username"):
        # Get the session username and set for the agent variable
        agent = session["username"].upper()

        # value of selection , sale, rent or all in searching dropdown
        search = request.args.get("search2")
        sort_by_selector = None
        select = None
        if search:
            select = search.replace("_", " ").capitalize()

        # Variables for type
        all_properties = None
        for_rent = None
        for_sale = None

        # Sort_by_selector variable is set by dropdown in my_adds.html template
        if search is None or search == "all_properties":

            # MongoDB Query for All properties
            all_properties = properties_collection.find({"agent": agent})
            sort_by_selector = all_properties

            # Pagination properties counter based into sort selector choose
            properties_pagination = all_properties.count()

        if search == "for_rent":

            # MongoDB Query for Rent
            for_rent = properties_collection.find(
                {"$and": [{"agent": agent}, {"rent_price": {"$gt": "1"}}]}
            )
            sort_by_selector = for_rent

            # Pagination properties counter based into sort selector choose
            properties_pagination = for_rent.count()

        if search == "for_sale":

            # MongoDB Query for Rent
            for_sale = properties_collection.find(
                {"$and": [{"agent": agent}, {"sale_price": {"$gt": "1"}}]}
            )
            sort_by_selector = for_sale

            # Pagination properties counter based into sort selector choose
            properties_pagination = for_sale.count()

        # Pagination
        properties_per_page = 6
        current_page = int(request.args.get("current_page", 1))
        num_pages = range(
            1, int(math.ceil(properties_pagination / properties_per_page)) + 1
        )
        properties = sort_by_selector.skip(
            (current_page - 1) * properties_per_page
        ).limit(properties_per_page)

        return render_template(
            "my_ads.html",
            sort_by_selector=sort_by_selector,
            for_sale=for_sale,
            for_rent=for_rent,
            properties=properties,
            current_page=current_page,
            search=search,
            select=select,
            pages=num_pages,
        )

    flash("You must be logged in to view this page.")
    return redirect(url_for("reg_login.login"))


@properties.route("/properties_list", methods=["GET", "POST"])
def list_properties():

    # Authentication is not necessary, the list of ads will be displayed to all users.

    # value of selection , sale, rent or all in searching dropdown
    search = request.args.get("search")
    sort_by_selector = None
    select = None
    if search:
        select = search.replace("_", " ").capitalize()

    # Variables for type
    all_properties = None
    for_rent = None
    for_sale = None

    # Sort_by_selector variable is set by dropdown in properties_listing.html template

    if search is None or search == "all_properties":
        all_properties = properties_collection.find(
            {"$or": [{"sale_price": {"$gt": "1"}}, {"rent_price": {"$gt": "1"}}]}
        )
        sort_by_selector = all_properties
        # Pagination properties counter based into sort selector choose
        properties_pagination = all_properties.count()
    if search == "for_rent":
        for_rent = properties_collection.find({"rent_price": {"$gt": "1"}})
        sort_by_selector = for_rent
        # Pagination properties counter based into sort selector choose
        properties_pagination = for_rent.count()
    if search == "for_sale":
        for_sale = properties_collection.find({"sale_price": {"$gt": "1"}})
        sort_by_selector = for_sale
        # Pagination properties counter based into sort selector choose
        properties_pagination = for_sale.count()

    # Pagination
    properties_per_page = 6
    current_page = int(request.args.get("current_page", 1))
    num_pages = range(
        1, int(math.ceil(properties_pagination / properties_per_page)) + 1
    )
    properties = sort_by_selector.skip((current_page - 1) * properties_per_page).limit(
        properties_per_page
    )

    return render_template(
        "properties_list.html",
        sort_by_selector=sort_by_selector,
        for_sale=for_sale,
        for_rent=for_rent,
        properties=properties,
        current_page=current_page,
        search=search,
        select=select,
        pages=num_pages,
    )


@properties.route("/property_details/<property_id>", methods=["GET", "POST"])
def property_details(property_id):

    # checks if there is a user logged in, if yes, the variable agent for check property is rendered
    if session.get("username"):
        property_details = properties_collection.find({"_id": ObjectId(property_id)})
        agent = session["username"].upper()
        return render_template(
            "property.html", property_details=property_details, agent=agent
        )

    property_details = properties_collection.find({"_id": ObjectId(property_id)})
    return render_template("property.html", property_details=property_details)
