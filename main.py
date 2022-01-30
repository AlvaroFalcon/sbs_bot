import os

from telegram import Update
import urllib.parse
from pyyoutube import Api, Video, VideoListResponse
import re
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, CallbackContext)

warned = []
commands = ["warn"]
banned_channel_ids = ["UCF3Ez6QwZwwr_E7RZGJMW0A"]
custom_commands = []
pattern_watch = 'https://www.youtube.com/watch?'
pattern_short = 'https://youtu.be/'
#api = Api(api_key='AIzaSyDrV2GZbXpKnRY5lx0ihQE4ansupC9krQE')
api = Api(api_key=os.getenv('API_KEY'))


def get_youtube_id_from_url(url):
    vid = ""
    if re.match(pattern_watch, url):
        yturl_qs = urllib.parse.urlparse(url).query
        vid = urllib.parse.parse_qs(yturl_qs)['v'][0]
    elif re.match(pattern_short, url):
        vid = url[17:28]
    return vid


def start(update, context):
    warned.append(str(update.message.from_user["username"]))
    context.bot.send_message(update.message.chat_id, warned)


def inmersion(update, context):
    context.bot.send_photo(update.message.chat_id, photo=open('inmersion.jpg', 'rb'))


def echo(update: Update, context: CallbackContext):
    message = update.message.text
    possible_command = message.split(" ")
    user = update.message.from_user["username"]

    if possible_command[0].startswith("!") in commands:
        manage_command(possible_command[0], possible_command[1])
        return

    if possible_command[0].startswith("!") in custom_commands:
        manage_custom_command(possible_command[0], possible_command[1])
        return

    handle_videos(message, context, update)


def manage_command(command, message):
    return


def manage_custom_command(command, message):
    return


def handle_videos(full_message, context: CallbackContext, update: Update):
    splitted_message = full_message.split(" ")
    for message in splitted_message:
        if re.match(pattern_watch, str(message)) or re.match(pattern_short, str(message)):
            youtube_id = get_youtube_id_from_url(message)
            video_by_id: VideoListResponse = api.get_video_by_id(video_id=youtube_id)
            video: Video = video_by_id.items[0]
            channel_id = video.snippet.channelId
            if channel_id in banned_channel_ids:
                context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
                context.bot.send_message(chat_id=update.effective_chat.id, text=str("Estos videos no se admiten aqui :("))
    return


def handle_banned_videos(message):
    return


def main():
    #TOKEN = "5172660367:AAGMCcn3csrVk86PDM_liMwxcHlWRe5Z4so"
    TOKEN = os.getenv('BOT_TOKEN')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('inmersion', inmersion))
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(echo_handler)
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()


if __name__ == '__main__':
    main()