########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->          WEB CRAWLER           <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import requests
import re

to_crawl = ['URL'] #LINK EX: http(s)://www.google.com.br/
crawled = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

while True:
    url = to_crawl[0]
    try:
        req = requests.get(url, headers=header)
    except:
        to_crawl.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    print 'Crawling:', url

    to_crawl.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            to_crawl.append(link)