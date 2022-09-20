import requests

async def get_waifu_image():
    response = await(requests.get("https://api.waifu.pics/sfw/waifu"))
    print(response.url)
    print(response.json())
