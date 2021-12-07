from telegram.ext import Updater
from telegram.ext import  CommandHandler, MessageHandler, Filters
import  os
import json
TOKEN = os.environ.get("TELEGRAM_ID")

def start(update, context):
    yourname = update.message.chat.first_name

    msg = "Hi "+yourname+"! Welcome to mimic bot."
    context.bot.send_message(update.message.chat.id, msg)


def mimic(update, context):
    context.bot.send_message(update.message.chat.id, update.message.text)

def details(update, context):
    print(type(update))
    obj = json.dumps(update, indent=3)
    print(type(obj))
    context.bot.send_message(update.message.chat.id, obj)

def error(update, context):
    context.bot.send_message(update.message.chat.id, "Oops! Error encountered!")

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("details", details))

    dp.add_handler(MessageHandler(Filters.text, mimic))


    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",port=os.environ.get("PORT",443),
                          url_path=TOKEN,
                          webhook_url="https://mimic-app.herokuapp.com/"+TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()

