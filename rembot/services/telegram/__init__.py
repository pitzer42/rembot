import os

from telegram.ext import Updater, MessageHandler, Filters, Handler

from rembot.services.telegram.events import MessageReceived


TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']


def attach(app):

    def handle(update, context):
        text = update.message.text
        chat = update.effective_chat.id
        receiver = context.bot
        event = MessageReceived(text, chat, receiver)
        app.notify(event)
    
    updater = Updater(TELEGRAM_BOT_TOKEN)
    handler = MessageHandler(Filters.all, handle)
    updater.dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()


def send_message(text, chat, bot):
    bot.send_message(text=text, chat_id=chat)
