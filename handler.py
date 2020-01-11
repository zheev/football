from bs4 import BeautifulSoup
import requests
from telegram import send_message

def get_html(html, one = False, tag = '', selector={}):
    soup = BeautifulSoup(html, 'html.parser')

    if one:
        list = soup
    else:
        list = soup.findAll(tag,selector)

    return list

def get_html_item_news(html):
    if len(html['href']):
        url = 'https://sport24.ru{}'.format(html['href'])
        r = requests.get(url)
        r.encoding = 'utf-8'
        html = get_html(r.text, True)

        return  html

def get_item_news(html_code):

        html = get_html_item_news(html_code)

        header = html.h1.text

        words = ''

        text = html.find(class_='js-mediator-article _1YOxdQ').find_all('span')

        for t in text:
            if t.find_parent('a'):
                t.extract()
            else:
                words = words + t.get_text()

        send_message(words, header)



def test_html(html):
    f = open('test.html', 'w')
    f.write(html)
    f.close()

def is_good_news(text):
    stop_word = ['жена', 'жену', 'развод', 'Уткин']
    if len(list(filter(lambda x: x in text, stop_word))) > 0:
        return False
    else:
        return True