import config

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters


def hello(update: Update, context):
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=update.effective_message.text
    )


def main():
    my_update = Updater(
        token=config.TOKEN,
        #base_url=config.PROXI,
        use_context=True
    )

    my_hendler = MessageHandler(Filters.all, hello)

    my_update.dispatcher.add_handler(my_hendler)

    my_update.start_polling()
    my_update.idle()


if __name__ == "__main__":
    main()
