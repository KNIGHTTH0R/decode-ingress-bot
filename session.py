import os
from tools import *
import inspect
import sys
from utils.functions import pprint
from tools import modules as modules

import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

logger = logging.getLogger(__name__)


class ImageCode(object):
    def __init__(self, file):
        self.file = file


class ModuleInfo(object):
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc
        self.methods = []

    def add(self, name, doc):
        self.methods.append((name, doc))


class DecodingSession(object):

    COMMANDS = {
        ('/back', '/b'): 'Go back to previous decoding step',
        ('/code', '/c'): 'Show current code',
        ('/help', '/h'): 'List of commands',
        ('/reset', '/r'): 'Reset decoding session',
        ('/set', '/s'): 'Set code'
    }

    def __init__(self, code):
        self.codes = [code]
        self.commands = {}
        self.info = []
        self._register_commands()

    def callback(self, bot, update, command, args):
        if command == 'back' or command == 'b':
            if len(self.codes) > 1:
                del self.codes[-1]
            self.reply(bot, update, self.codes[-1])
            return

        if command == 'reset' or command == 'r':
            self.codes = [self.codes[0]]
            self.reply(bot, update, self.codes[0])
            return

        if command == 'code' or command == 'c':
            self.reply(bot, update, self.codes[-1])
            return

        if command == 'set' or command == 's':
            if not args:
                self.reply(bot, update, "You must specify a passcode")
                return
            self.codes.append(' '.join(args))
            self.reply(bot, update, self.codes[-1])
            return

        if command == 'help' or command == 'h':
            messages = []

            r = "Session commands\n\n" + \
                "\n".join(["{} - {}".format(" or ".join(list(k)), v) for k,v in DecodingSession.COMMANDS.items()]) + \
                "\n\n"
            for module in self.info:
                m = ""
                m += (module.doc or "None") + "\n"
                m += "\n".join(["/{} - {}".format(command[0], command[1]) for command in module.methods])
                m += "\n\n"
                if (len(r) + len(m)) > 4096:
                    messages.append(r)
                    r = m
                else:
                    r += m
            messages.append(r)
            for message in messages:
                bot.sendMessage(update.message.chat_id, text=message)
            return

        if command == 'botfather':
            messages = []

            commands = ["new - Start new decoding session", "cancel - Cancel current decoding session"]
            for k, v in DecodingSession.COMMANDS.items():
                commands.append("{} - {}".format(list(k)[0][1:], v))
            for module in self.info:
                module_commands = ["{} - {}".format(command[0], command[1]) for command in module.methods]
                if len("\n".join(commands)) + len("\n".join(module_commands)) > 4096:
                    messages.append("\n".join(commands))
                    commands = module_commands
                else:
                    commands += module_commands
            messages.append("\n".join(commands))
            for message in messages:
                bot.sendMessage(update.message.chat_id, text=message)
            # self.reply(bot, update, "\n".join(commands))
            return

        if command in self.commands:
            code = self.commands[command](self.codes[-1], *args)
            if getattr(self.commands[command], '__store__', True) and not type(code) is ImageCode:
                self.codes.append(code)
            self.reply(bot, update, code)

    def reply(self, bot, update, what):

        if type(what) is ImageCode:
            try:
                bot.sendPhoto(update.message.chat_id, photo=open(what.file, 'rb'))
            finally:
                os.remove(what.file)
            return

        for c in pprint(what):
            bot.sendMessage(update.message.chat_id, text=c, parse_mode='markdown')

    def _register_commands(self):
        try:
            for module in modules:
                module_info = ModuleInfo(module, sys.modules[module].__doc__)
                for (name, func) in inspect.getmembers(sys.modules[module], inspect.isfunction):
                    if getattr(func, '__command_name__', None):
                        cname = getattr(func, '__command_name__')
                        self.commands[cname] = func
                        module_info.add(cname, func.__doc__)
                self.info.append(module_info)
        except Exception as e:
            logger.error("Could not register commands")
