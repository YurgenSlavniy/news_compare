# Собираю новости с сайта https://ria.ru/

from lxml import html
import requests
from pprint import pprint

url_ria = 'https://ria.ru/'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response = requests.get(url_ria, headers=headers)
dom_ria = html.fromstring(response.text)
news_ria = dom_ria.xpath("//span[@class='cell-list__item-title']/text()")

pprint(news_ria[:5])


# Собираю новости с сайта https://regnum.ru/

from lxml import html
import requests
from pprint import pprint

url_regnum = 'https://regnum.ru/'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response_regnum = requests.get(url_regnum , headers=headers)
dom_regnum = html.fromstring(response_regnum.text)
news_regnum = dom_regnum.xpath("//span[@class='article-title']/text()")

pprint(news_regnum[:5])

clear_news_list = []

for el in news_regnum:
    new_el = el.replace('\n', '')
    if new_el != '                        ' and new_el != '                                        ':
        clear_news_list.append(new_el)
    else:
        continue
      

# Собираю новости с сайта https://www.interfax.ru/

from lxml import html
import requests
from pprint import pprint

url_interfax = 'https://www.interfax.ru/'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response_interfax = requests.get(url_interfax , headers=headers)
dom_interfax = html.fromstring(response_interfax.text)
news_interfax = dom_interfax.xpath("//h3/text()")

pprint(news_interfax[:5])

# Собираю новости с сайта https://tass.ru/

from lxml import html
import requests
from pprint import pprint

url_tass = 'https://tass.ru/'
headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

response_tass = requests.get(url_tass , headers=headers)
dom_tass = html.fromstring(response_tass.text)
news_tass = dom_tass.xpath("//span[contains(@class, 'ds_ext_title')]/text()")

clear_news_tass = []
for el in news_tass:
    clear_news_tass.append(el.replace('\xa0', ''))
    
pprint(clear_news_tass[4:9])




