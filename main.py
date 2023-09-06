import os
import string
from telegram import Update
from command_manager import command_manager
from url_utils import url_utils
import urllib.parse
from youtube_utils import youtube_utils
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)

def start(update, context):
    return

def inmersion(update, context):
    context.bot.send_photo(update.message.chat_id, photo=open('inmersion.jpg', 'rb'))

def echo(update: Update, context: CallbackContext):
    message: str = update.message.text
    
    possible_command = message.split(" ")    
    if command_manager.is_command(possible_command[0]):
        command_manager.manage_command(possible_command[0], possible_command, context, update)
        return
			
    handle_splitted_message(message, context, update)
    check_entities(update.message.entities, context, update)
    
def check_entities(entities, context, update):
		for entity in entities:
				print(entity)
				if entity.type == "text_link":
						message = entity.url
						if not url_utils.is_url(message.strip()):
								print("not url")
								continue
						message = url_utils.get_url_from_shortener(message)
						if youtube_utils.is_youtube_url(message):
								youtube_utils.manage_youtube_vid(message, context, update)
		return
    
def handle_splitted_message(full_message, context: CallbackContext, update: Update):        
    splitted_message = url_utils.formatTextToOneLine(full_message)
    splitted_message = splitted_message.split(" ")
    for message in splitted_message:
        if not url_utils.is_url(message.strip()):
            print("not url")
            continue
        message = url_utils.get_url_from_shortener(message)
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
