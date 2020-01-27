import requests
from handler import get_item_news, get_html, is_good_news


if __name__ == '__main__':
    r = requests.get('https://sport24.ru/football')

    r.encoding = 'utf-8'

    news_list = get_html(r.text, False, 'a', {'class':"qNoPjs"})

    for item in news_list:
        if is_good_news(item.span.text):
            get_item_news(item)
            break