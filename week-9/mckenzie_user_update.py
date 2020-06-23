# ============================================
# Title: Exercise 9.3
# Author: Diandra McKenzie
# Date: 23 June 2020
# Description: Updating and Querying Documents
# ============================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

# update user document by changing email field
db.users.update_one(

    {"employee_id": "0000008"},

    {
        "$set": {
            "email": "damckenzie@my365.bellevue.edu"
        }
    }
)

# output the following fields : email, employee_id, first_name, last_name

pprint.pprint(db.users.find_one(

    {"employee_id":"0000008"},

    {
        "email":1, 
        "employee_id":1, 
        "first_name":1, 
        "last_name":1, 
        "_id":0
        }
    )
)