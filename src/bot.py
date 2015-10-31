"""
Bot to log all the things from TwitchInstallsArchLinux

by shane Engelman (me@5h4n3.com)
"""

import lib.irc as irc_
from lib.functions_general import *
import lib.functions_commands as commands
import src.lib.command_headers
import src.lib.cron as cron
import sys
import datetime
import traceback
import sched
import time
import threading
from src.lib.twitch import USER, MESSAGE
from src.lib.queries import insert_message

END = False

class Roboraj(object):

    def __init__(self, config):
        self.config = config
        src.lib.command_headers.initalizeCommands(config)
        self.irc = irc_.irc(config)

        # start threads for channels that have cron messages to run
        cron.initialize(self.irc, self.config.get("cron", {}))

    def run(self):

        config = self.config
        while True:
            try:
                data = self.irc.nextMessage()
                if not self.irc.check_for_message(data):
                    continue

                message_dict = self.irc.get_message(data)
                channel = message_dict['channel']
                message = message_dict['message']
                username = message_dict['username']
                message_dict['time'] = time.time()
                sent_at = message_dict['time']
                resp0 = '%s' % (username)
                resp1 = '%s' % (channel)
                resp2 = '%s' % (message)
                USER = username
                MESSAGE = message.decode('utf-8')
                try:
                    insert_message(USER, MESSAGE)
                except Exception as err:
                    print ">>> ERROR:", err
                part = message.split(' ')[0]
                valid = False
                if commands.is_valid_command(message):
                    valid = True
                if commands.is_valid_command(part):
                    valid = True
                if not valid:
                    continue

                self.handleCommand(part, channel, username, message)
            except Exception as err:
                raise
                traceback.print_exc(file=self.log)

    def handleCommand(self, command, channel, username, message):
        # parse arguments
        # if command is space case then
        #   !foo bar baz
        # turns into
        #   command = "!foo", args=["bar baz"]
        # otherwise it turns into
        #   command = "!foo", args=["bar", "baz:]
        # print("Inputs:", command, channel, username, message)
        if command == message:
            args = []

        elif command == message and command in commands.keys():
            print "Yes, it is in commands"

        else:
            # default to args = ["bar baz"]
            args = [message[len(command) + 1:]]

        if not commands.check_is_space_case(command) and args:
            # if it's not space case, break the arg apart
            args = args[0].split(" ")

        # check cooldown.
        if commands.is_on_cooldown(command, channel):
            pbot('Command is on cooldown. (%s) (%s) (%ss remaining)' % (
                command, username, commands.get_cooldown_remaining(command, channel)),
                channel
            )
            return
        pbot('Command is valid and not on cooldown. (%s) (%s)' %
             (command, username), channel)

        # Check for and handle the simple non-command case.
        cmd_return = commands.get_return(command)
        if cmd_return != "command":
            # it's a return = "some message here" kind of function
            resp = '(%s) : %s' % (username, cmd_return)
            commands.update_last_used(command, channel)
            self.irc.send_message(channel, resp)
            return


        result = commands.pass_to_function(command, args)
        commands.update_last_used(command, channel)

        if result:
            resp = '(%s) : %s' % (username, result)
            pbot(resp, channel)
            self.irc.send_message(channel, resp)
