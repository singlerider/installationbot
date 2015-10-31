from pymongo import MongoClient
from src.bot import USER, MESSAGE
from time import time

client = MongoClient()

client = MongoClient("mongodb://mongodb0.example.net:27019")

db = client.primer

db = client['primer']

db.dataset
db['dataset']

coll = db.dataset
coll = db['dataset']

"""

dict = {
        USER: {
            "points": 0,
            "time_in_chat": 0,
            {
            MESSAGE: {
                "timestamp": [],
                "counter": 0
                }
            }
        }
    }

#### Example Data Structure
users = {
        USER: {
            messages: {
                MESSAGE: {
                    "timestamp": [],
                    "counter": 0
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
"""
"""
users = {}
messages = {}
"""
def new_user():
    """
    users[USER] = {
        "messages": {
            MESSAGE: {
                "timestamp" = [time()],
                "counter" = 1
                }
            }
        "points": 0,
        "time_in_chat": 0
        }
    messages[MESSAGE] = {
        users: {
            USER: 0
        }
        "timestamp": [time()],
        "counter": += 1
    }
    """
    pass

def insert_message():
    """
    if USER not in users:
        new_user()
    else:
        users[USER] = {
            "messages": {
                MESSAGE: {
                    "timestamp" = [time()],
                    "counter" += 1
                    }
                }
            }
        messages[MESSAGE] = {
            users: {
                USER: += 1
            }
            "timestamp": [time()],
            "counter": += 1
        }
    """
    pass

def count_messages():
    """
    len(messages[MESSAGE])
    """
    pass

def count_message(message):
    """
    messages[message]["counter"]
    """
    pass

def message_times(message):
    """
    users[USER][messages][message]["timestamp"]
    """
    pass

def count_user_messages(user):
    """
    len(users[user][messages])
    """
    pass
