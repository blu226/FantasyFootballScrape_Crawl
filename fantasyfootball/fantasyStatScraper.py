import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import urllib.parse
import urllib.error
import socket
import ssl
import lxml
import pickle


# values so websites don't think I am a crawler and deny me access
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
values = {'name' : 'CS485_crawl',
          'location' : 'Lexington',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }


class weeklyCrawler():

    def __init__(self):
        self.url = "https://www.fantasydata.com/nfl-stats/daily-fantasy-football-salary-and-projection-tool?"
        self.stats = {}

    def crawl(self):

        for season in range(2002, 2018):
            for team in range(0, 31):
                for position in range(2, 7):
                    for week in range(1, 16):

                        url_to_crawl = self.url + "position=" + str(position) + "&team=" + str(team) + "&season=" + str(season)
                        url_to_crawl += "&seasontype=1&scope=2&startweek=" + str(week) + "&endweek=" + str(week)

                        context = ssl.create_default_context()
                        context.check_hostname = False
                        context.verify_mode = ssl.CERT_NONE
                        data = urllib.parse.urlencode(values).encode('utf-8')
                        req = urllib.request.Request(url_to_crawl, data, headers)

                        try:
                            response = urllib.request.urlopen(req, context=context)

                            #soup = BeautifulSoup(response, "html.parser")

                            html = response.read()
                            #print(html)
                            data = pd.read_html(html)   # error thrown No tables found

                            #data = pd.DataFrame(data[0])
                            #cols = data.values[-1].tolist()

                            #data.columns = cols
                            #data["pos"] = "null"
                            #data["proj"] = "null"
                            #data["salary"] = "null"
                            #data.drop(data.tail(1).index, inplace=True)

                            #print(data)

                            # pickle.dump(data, open("./weeklyData/season" + str(year) + "week" + str(week) + str(category) + ".pkl", "wb"))

                        except (urllib.error.URLError, ValueError, ConnectionResetError, ConnectionError, TimeoutError, ConnectionRefusedError, socket.timeout) as e:
                            print("ERROR:", e)


crawl = weeklyCrawler()
crawl.crawl()

