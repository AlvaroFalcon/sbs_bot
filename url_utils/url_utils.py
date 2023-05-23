import re
import string
import requests

url_regex = '^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&\'\(\)\*\+,;=.]+$'

def is_url(message):
    is_match = re.match(re.compile(url_regex), message)
    print(is_match)
    return is_match is not None or "http" in message

def get_url_from_shortener(message):
    messageCopy = str(message)
    if(not hasSchema(messageCopy)):
        messageCopy = addSchema(messageCopy)
    try:
        response = requests.get(messageCopy)
        return response.url
    except Exception as e:
        return messageCopy

def hasSchema(text: str):
    return "https" in text or "http" in text

def addSchema(text: str):
    return "http://"+text

def formatTextToOneLine(text: str):
    result = " ".join(line.strip() for line in text.splitlines())
    return eval(repr(result))