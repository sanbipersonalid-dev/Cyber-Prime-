import requests
from telegram.ext import *

TOKEN = "8661757577:AAHfk3kmKrBsnsIfCvcYGTDO9erjBd3-_Fk"

def reply(update, context):
    text = update.message.text

    url = "https://mahfuzahmedchy.com/wrom.php?text=" + text

    data = requests.get(url).json()

    update.message.reply_text(data["response"])

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, reply))

updater.start_polling()
updater.idle()
