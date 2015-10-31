from pymongo import MongoClient
from time import time

client = MongoClient()

client = MongoClient("127.0.0.1:27017")

db = client.twitch
collection = db.users

coll = db.dataset
coll = db['dataset']

"""
#### Example Data Structure
users = {
        USER: {
            messages: {
                MESSAGE: {
                    "timestamp": [],
                    "counter": 0
                    ""
                }
            },
            "points": 0,
            "time_in_chat": 0
            }
        }
messages = {
            MESSAGE: {
                users: {
                    USER: True,
                },
                "timestamp": [],
                "counter": 0
                }
            }

            users["shane"]["messages"]["uniquemessage"] = {"timestamp": [145.324], "counter": 1}
"""

users = {}
messages = {}

def new_user(user, message):
    result = db.users.insert_one(
    {user: {
        "messages": {
            message: {
                "timestamp": [time()],
                "counter": 1
                },
            },
        "points": 0,
        "time_in_chat": 0
        }
    }
    )
    messages[message] = {
        "users": {
            user: 0
        },
        "timestamp": [time()],
        "counter": 1
        }

def insert_message(user, message):
    new_user(user, message)
    """if message not in users[user]["messages"]:
        users[user]["messages"][message] = {
                    "timestamp": [time()],
                    "counter": 1
                    }
        messages[message] = {
            users: {
                user: 1
            },
            "timestamp": [time()],
            "counter": 1
        }"""


def count_messages(message):
    len(messages[message])


def count_message(message):
    messages[message]["counter"]


def message_times(user, message):
    users[user]["messages"][message]["timestamp"]


def count_user_messages(user):
    len(users[user]["messages"])
