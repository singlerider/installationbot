from src.lib.twitch import *

def viewers():
    user_dict, all_users = get_dict_for_users()
    chatter_count = user_dict['chatter_count']
    return all_users


def cron(channel):
    user_dict, all_users = get_dict_for_users()
    return get_dict_for_users()
