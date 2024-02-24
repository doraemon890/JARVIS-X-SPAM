from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import BOT_TOKEN

# Define your Telegram bot token here
TOKEN = BOT_TOKEN

def broadcast_message(update: Update, context: CallbackContext) -> None:
    message = ' '.join(context.args)
    for chat_id in context.bot.get_updates()[0].message.chat_id:
        context.bot.send_message(chat_id=chat_id, text=message)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('broadcast', broadcast_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
