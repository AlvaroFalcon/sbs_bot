import urllib.parse
import re
from pyyoutube import Api, Video, VideoListResponse

pattern_watch = 'https://www.youtube.com/watch?'
pattern_short = 'https://youtu.be/'
banned_channel_ids = ["UCF3Ez6QwZwwr_E7RZGJMW0A"]
api = Api(api_key='AIzaSyDrV2GZbXpKnRY5lx0ihQE4ansupC9krQE')

def _get_youtube_id_from_url(url):
    vid = ""
    if re.match(pattern_watch, url):
        yturl_qs = urllib.parse.urlparse(url).query
        vid = urllib.parse.parse_qs(yturl_qs)['v'][0]
    elif re.match(pattern_short, url):
        vid = url[17:28]
    return vid


def is_youtube_url(message):
    return re.match(pattern_watch, message) or re.match(pattern_short, message)

def manage_youtube_vid(url, context, update):
    youtube_id = _get_youtube_id_from_url(url)
    video_by_id: VideoListResponse = api.get_video_by_id(video_id=youtube_id)
    video: Video = video_by_id.items[0]
    channel_id = video.snippet.channelId
    if channel_id in banned_channel_ids:
        try:
            context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            context.bot.send_message(chat_id=update.effective_chat.id, text=str("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))                
        except:
            print("Trying to delete an empty message")
