import requests
from const import TOKEN_APP

def getUrl(TOKEN, type):
    return "https://api.telegram.org/bot{0}/{1}".format(TOKEN, type)

def send_message(text, header):
    url = getUrl(TOKEN_APP, 'sendMessage')
    requests.post(url, data={'chat_id': '@zheevfootball', 'text': '\t\t **{}** \n{}'.format(header,text),
                             'parse_mode': 'Markdown'})