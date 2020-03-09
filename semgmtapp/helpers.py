from bson.objectid import ObjectId
from semgmtapp.ext.database import mongo

# DB Collections
properties_collection = mongo.db.properties
users_collection = mongo.db.users


# Properties Type Dropdown List
def dropdown_properties_type():
    property_type_list = ["Apartment", "House", "Other"]
    return property_type_list


# Num beds Dropdown List
def dropdown_num_beds():
    num_bed_list = ["1 bedroom", "2 bedrooms", "3 bedrooms", "4 bedrooms"]
    return num_bed_list


# Num baths Dropdown List
def dropdown_num_baths():
    num_bath_list = ["1 bathroom", "2 bathrooms", "3 bathrooms", "4 bathrooms"]
    return num_bath_list


# Districts Dropdown List
def dropdown_districts():
    district_list = ["Eastleigh", "Fareham", "Havant", "Portsmouth", "Other"]
    return district_list
