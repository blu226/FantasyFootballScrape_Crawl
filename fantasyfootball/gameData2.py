import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import urllib.parse
import urllib.error
import socket
import ssl
import lxml


# values so websites don't think I am a crawler and deny me access
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
values = {'name' : 'CS485_crawl',
          'location' : 'Lexington',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }


class weeklyCrawler():

    def __init__(self):
        self.url = "http://www.nfl.com/stats/weeklyleaders?"
        self.stats = {}

    def crawl(self):

        for year in range(1970, 2019):
            for week in range(1, 18):
                for category in ["Passing", "Rushing", "Receiving"]:

                    url_to_crawl = self.url + "week=" + str(week) + "&season="  + str(year) + "&showCategory=" + category

                    context = ssl.create_default_context()
                    context.check_hostname = False
                    context.verify_mode = ssl.CERT_NONE
                    data = urllib.parse.urlencode(values).encode('utf-8')
                    req = urllib.request.Request(url_to_crawl, data, headers)

                    try:
                        response = urllib.request.urlopen(req, timeout=5, context=context)
                        html = response.read()

                        data = pd.read_html(html)
                        print(data)

                    except (urllib.error.URLError, ValueError, ConnectionResetError, ConnectionError, TimeoutError, ConnectionRefusedError, socket.timeout) as e:
                        print("ERROR:", e)


crawl = weeklyCrawler()
crawl.crawl()

