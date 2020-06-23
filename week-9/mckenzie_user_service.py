# ============================================
# Title: Exercise 9.2
# Author: Diandra McKenzie
# Date: 22 June 2020
# Description: Querying and Creating Documents
# ============================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

# create a  new user

user = {

    "first_name": "Claude",

    "last_name": "Debussy",

    "email": "cdebussy@me.com",

    "employee_id": "0000008",

    "date_created": datetime.datetime.utcnow()

}

# insert a new user

user_id = db.users.insert_one(user).inserted_id

# output the auto-generated user_id

print(user_id)

# query the users collection using the "find_one()" method
# print the document returned from the FindOne Query

pprint.pprint(db.users.find_one())