# -*- coding: utf-8 -*-
import psycopg2
import sys
from time import time

con = None

try:

    con = psycopg2.connect(database='twitchinstalls', user='postgres')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver


except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

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

            users["postgres"]["messages"]["uniquemessage"] = {"timestamp": [145.324], "counter": 1}
"""

users = {}
messages = {}

def new_user(user, message):
    pass

def insert_message(user, message):
     with con:

        cur = con.cursor()
        cur.execute("""
        INSERT INTO users
        SELECT	*
        FROM	(VALUES (%s, %s, %s)) tbl(username, points, time_in_chat)
        WHERE NOT EXISTS(
        				SELECT	0
        				FROM	users
        				WHERE	tbl.username = users.username
        				);""",
                    [user, 0, 0])
        cur.execute("""INSERT INTO messages (username, message, time_stamp)
        VALUES (%s, %s, %s)""", [user, message, time()])


def count_messages(message):
    len(messages[message])


def count_message(message):
    messages[message]["counter"]


def message_times(user, message):
    users[user]["messages"][message]["timestamp"]


def count_user_messages(user):
    len(users[user]["messages"])
