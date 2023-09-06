import requests

def get_waifu_image(context, update):
    response = requests.get("https://api.waifu.pics/sfw/waifu")
    send_to_channel(context, update, str(response.json()["url"]))	
def get_neko(context, update):
    response = requests.get("https://api.waifu.pics/sfw/neko") 
    send_to_channel(context, update, str(response.json()["url"]))	
def get_shinobu(context, update):
	response = requests.get("https://api.waifu.pics/sfw/shinobu") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_megumin(context, update):
	response = requests.get("https://api.waifu.pics/sfw/megumin") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_bully(context, update):
	response = requests.get("https://api.waifu.pics/sfw/bully") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_cuddle(context, update):
	response = requests.get("https://api.waifu.pics/sfw/cuddle") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_cry(context, update):
	response = requests.get("https://api.waifu.pics/sfw/cry") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_hug(context, update):
	response = requests.get("https://api.waifu.pics/sfw/hug") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_awoo(context, update):
	response = requests.get("https://api.waifu.pics/sfw/awoo") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_kiss(context, update):
	response = requests.get("https://api.waifu.pics/sfw/kiss") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_lick(context, update):
	response = requests.get("https://api.waifu.pics/sfw/lick") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_pat(context, update):
	response = requests.get("https://api.waifu.pics/sfw/pat") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_smug(context, update):
	response = requests.get("https://api.waifu.pics/sfw/smug") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_bonk(context, update):
	response = requests.get("https://api.waifu.pics/sfw/bonk") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_yeet(context, update):
	response = requests.get("https://api.waifu.pics/sfw/yeet") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_blush(context, update):
	response = requests.get("https://api.waifu.pics/sfw/blush") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_smile(context, update):
	response = requests.get("https://api.waifu.pics/sfw/smile") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_wave(context, update):
	response = requests.get("https://api.waifu.pics/sfw/wave") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_highfive(context, update):
	response = requests.get("https://api.waifu.pics/sfw/highfive") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_handhold(context, update):
	response = requests.get("https://api.waifu.pics/sfw/handhold") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_kick(context, update):
	response = requests.get("https://api.waifu.pics/sfw/kick") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_kill(context, update):
	response = requests.get("https://api.waifu.pics/sfw/kill") 
	send_to_channel(context, update, str(response.json()["url"]))		
def get_happy(context, update):
	response = requests.get("https://api.waifu.pics/sfw/happy") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_wink(context, update):
	response = requests.get("https://api.waifu.pics/sfw/wink") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_dance(context, update):
	response = requests.get("https://api.waifu.pics/sfw/dance") 
	send_to_channel(context, update, str(response.json()["url"]))	
def get_cringe(context, update):
	response = requests.get("https://api.waifu.pics/sfw/cringe") 
	send_to_channel(context, update, str(response.json()["url"]))	

def send_to_channel(context, update, document):
	print(document)
	if ".gif" in document:
		context.bot.sendDocument(chat_id=update.effective_chat.id, document = document)
	else:
		context.bot.send_photo(chat_id=update.effective_chat.id, photo=document)
