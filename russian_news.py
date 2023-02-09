# Собираю новости с сайта https://ria.ru/

from lxml import html
import requests
from pprint import pprint

url_ria = 'https://ria.ru/'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response = requests.get(url_ria, headers=headers)

dom_ria = html.fromstring(response.text)

news = dom_ria.xpath("//span[@class='cell-list__item-title']/text()")

