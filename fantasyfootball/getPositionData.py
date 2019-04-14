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
        self.url = "https://www.pro-football-reference.com/years/"
        self.stats = {}

    def crawl(self):

        for year in range(1993, 2019):
            print("YEAR:", year)
            for category in ["passing", "rushing", "receiving"]:

                url_to_crawl = self.url + str(year) + "/" + str(category) + ".htm"

                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                data = urllib.parse.urlencode(values).encode('utf-8')
                req = urllib.request.Request(url_to_crawl, data, headers)

                try:
                    response = urllib.request.urlopen(req, context=context)
                    html = response.read()

                    data = pd.read_html(html)

                    data = pd.DataFrame(data[0])

                    if category == "rushing":
                        data.columns = data.columns.droplevel(0)

                    elif category == "passing":
                        data.drop(data.head(1).index, inplace=True)

                    for index, row in data.iterrows():
                        name = str(row["Player"]).replace("*", "")
                        name = name.replace("+", "")
                        for week in range(1, 18):
                            for pkl_category in ["Passing", "Rushing", "Receiving"]:

                                loaded_data = pickle.load(open("./weeklyData/season" + str(year) + "week" + str(week) + pkl_category + ".pkl", "rb"))
                                for pkl_index, pkl_row in loaded_data.iterrows():
                                    if pkl_row["Name"] == name:
                                        pos = row["Pos"]
                                        if isinstance(pos, str):
                                            pos_arr = pos.split("/")
                                            pkl_row["pos"] = pos_arr[0].upper()
                                            break

                                pickle.dump(loaded_data, open("./weeklyData/season" + str(year) + "week" + str(week) + pkl_category + ".pkl", "wb"))

                except (urllib.error.URLError, ValueError, ConnectionResetError, ConnectionError, TimeoutError, ConnectionRefusedError, socket.timeout) as e:
                    print("ERROR:", e)


crawl = weeklyCrawler()
crawl.crawl()

