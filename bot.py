#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from telegram.ext import Updater, CommandHandler, Handler
import logging
from telegram import Bot, Update
import inspect
import sys
from session import DecodingSession
from secrets import TG_BOT_TOKEN


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)


class DecoderBot(Bot):
    def __init__(self, token):
        super(DecoderBot, self).__init__(token)
        self.sessions = {}


class DecodeCommandHandler(Handler):
    def __init__(self):
        super(DecodeCommandHandler, self).__init__(None, False)

    def check_update(self, update):
        return (isinstance(update, Update) and
                update.message and
                update.message.text and
                update.message.text.startswith('/'))

    def handle_update(self, update, dispatcher):
        optional_args = self.collect_optional_args(dispatcher)
        optional_args['args'] = update.message.text.split(' ')[1:]
        optional_args['command'] = update.message.text[1:].split(' ')[0].split('@')[0]
        if update.message.chat_id in dispatcher.bot.sessions:
            dispatcher.bot.sessions[update.message.chat_id].callback(dispatcher.bot, update, **optional_args)
        else:
            dispatcher.bot.sendMessage(update.message.chat_id, text="There is no decoding session running. Start one with /new")


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def new(bot, update, args):
    chat_id = update.message.chat_id
    if chat_id in bot.sessions:
        bot.sendMessage(chat_id, text="A decoding sessions is already started. "
                                      "You cannot start a new one unless you /cancel the existing one")
        return

    if not args or len(args) < 1:
        bot.sendMessage(chat_id, text="To start a decoding session you MUST add a code to start with")
    else:
        bot.sessions[chat_id] = DecodingSession(" ".join(args))
        bot.sendMessage(chat_id, text="Decoding session started!")


def cancel(bot, update):
    chat_id = update.message.chat_id
    if chat_id in bot.sessions:
        del bot.sessions[chat_id]
        bot.sendMessage(chat_id, text="Current decoding session canceled. Use /new to start a new session")
    else:
        bot.sendMessage(chat_id, text="There is no decoding session running. Start one with /new")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    bot = DecoderBot(TG_BOT_TOKEN)
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(bot=bot)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("new", new, pass_args=True))
    dp.add_handler(CommandHandler("cancel", cancel))

    dp.add_handler(DecodeCommandHandler())

    try:
        import commands.basic

        # Register commands
        for (name, func) in inspect.getmembers(sys.modules['commands.basic'], inspect.isfunction):
            if getattr(func, '__command_handler__', False):
                logger.info("Register command /{}".format(name))
                dp.add_handler(CommandHandler(name, func, pass_args=True))
    except Exception:
        logger.error("Could not register commands")

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
