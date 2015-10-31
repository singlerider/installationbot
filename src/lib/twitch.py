import requests
import json
import random
import datetime
from src.bot import *

USER = ""
MESSAGE = ""

def get_dict_for_users():
    get_dict_for_users_url = 'http://tmi.twitch.tv/group/user/twitchinstallsarchlinux/chatters'
    get_dict_for_users_resp = requests.get(url=get_dict_for_users_url)
    try:
        users = json.loads(get_dict_for_users_resp.content)
    except:
        return "Twitch's backend is down. Sorry. Treats will return once that gets fixed."
    user_dict = users
    all_users = []
    for user in users['chatters']['moderators']:
        all_users.append(str(user))
    for user in users['chatters']['viewers']:
        all_users.append(str(user))
    for user in users['chatters']['staff']:
        all_users.append(str(user))
    for user in users['chatters']['admins']:
        all_users.append(str(user))
    return user_dict, all_users


def get_stream_status():
    get_stream_status_url = 'https://api.twitch.tv/kraken/streams/twitchinstallsarchlinux'
    get_stream_status_resp = requests.get(url=get_stream_status_url)
    online_data = json.loads(get_stream_status_resp.content)
    if online_data["stream"] != None:
        return True


def get_stream_uptime():
    if get_stream_status():
        format = "%Y-%m-%d %H:%M:%S"
        get_stream_uptime_url = 'https://api.twitch.tv/kraken/streams/twitchinstallsarchlinux'
        get_stream_uptime_resp = requests.get(url=get_stream_uptime_url)
        uptime_data = json.loads(get_stream_uptime_resp.content)
        start_time = str(uptime_data['stream']['created_at']).replace(
            "T", " ").replace("Z", "")
        stripped_start_time = datetime.datetime.strptime(start_time, format)
        time_delta = datetime.datetime.utcnow() - stripped_start_time
        return str(time_delta)
    else:
        return "The streamer is offline, duh."


def get_online_status():
    get_online_status_url = 'https://api.twitch.tv/kraken/streams/twitchinstallsarchlinux'
    get_online_status_resp = requests.get(url=get_online_status_url)
    online_data = json.loads(get_online_status_resp.content)
    if online_data["stream"] != None:
        return True


def get_stream_followers():
    url = 'https://api.twitch.tv/kraken/channels/twitchinstallsarchlinux/follows?limit=100'
    resp = requests.get(url=url)
    data = json.loads(resp.content)
    return data
