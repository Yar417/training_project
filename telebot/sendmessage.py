import requests
from .models import TeleSettings

token = '5121272763:AAGO35cOcTa-K0gMtrIppp23gu0OXWYxcD4'
chat_id = '-768899510'
text = 'test_2'


def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text,
    })