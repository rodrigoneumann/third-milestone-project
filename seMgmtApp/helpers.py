from bson.objectid import ObjectId
from seMgmtApp.ext.database import mongo

#DB Collections
properties_collection = mongo.db.properties
users_collection = mongo.db.users

# Properties Type Dropdown List
def dropdown_properties_type():
    property_type_list = properties_collection.distinct("property_type")
    return property_type_list

# Num beds Dropdown List
def dropdown_num_beds():
    num_bed_list = properties_collection.distinct("num_bed")
    return num_bed_list

# Num baths Dropdown List
def dropdown_num_baths():
    num_bath_list = properties_collection.distinct("num_bath")
    return num_bath_list

# Districts Dropdown List
def dropdown_districts():
    district_list = properties_collection.distinct("district")
    return district_list