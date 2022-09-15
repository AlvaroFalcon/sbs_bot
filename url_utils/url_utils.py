import re
import string
import requests

url_regex = '^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$'

def is_url(message):
    is_match = re.match(re.compile(url_regex), message)
    return is_match is not None

def get_url_from_shortener(message):
    try:
        response = requests.get(message)
        return response.url
    except:
        return message