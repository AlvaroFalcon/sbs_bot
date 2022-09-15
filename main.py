import os
import string
from telegram import Update
import command_manager
import urllib.parse
import url_utils
import youtube_utils
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)

def start(update, context):
    return

def inmersion(update, context):
    context.bot.send_photo(update.message.chat_id, photo=open('inmersion.jpg', 'rb'))

def echo(update: Update, context: CallbackContext):
    message = update.message.text
    possible_command = message.split(" ")
    if command_manager.is_command():
        command_manager.manage_command(possible_command[0], possible_command[1])
        return

    handle_splitted_message(message, context, update)

def handle_splitted_message(full_message, context: CallbackContext, update: Update):
    splitted_message = full_message.split(" ")
    for message in splitted_message:
        if not url_utils.is_url(message):
            continue
        message = url_utils.get_url_from_shortener(update, context, message)
        if youtube_utils.is_youtube_url(message):
            youtube_utils.manage_youtube_vid(message, context, update)
    return

def handle_banned_videos(message):
    return

def main():
    TOKEN = "5172660367:AAGMCcn3csrVk86PDM_liMwxcHlWRe5Z4so"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('inmersion', inmersion))
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
