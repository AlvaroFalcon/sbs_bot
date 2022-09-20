import requests

def get_waifu_image(context, update):
    response = requests.get("https://api.waifu.pics/sfw/waifu")    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=str(response.json()["url"]))