import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import urllib.parse
import urllib.error
import socket
import ssl
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import lxml
import pickle
import html5lib


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

        for season in range(2018, 2019):
            for team in range(0, 1):
                for position in range(2, 3):
                    for week in range(1, 2):


                        url_to_crawl = self.url + "position=" + str(position) + "&team=" + str(team) + "&season=" + str(season)
                        url_to_crawl += "&seasontype=1&scope=2&startweek=" + str(week) + "&endweek=" + str(week)

                        print(url_to_crawl)

                        try:

                            options = Options()
                            options.headless = True
                            browser = webdriver.Firefox(options=options)
                            browser.get(url_to_crawl)
                            html = browser.page_source
                            data = pd.read_html(html)
                            rows_list = []
                            for index, row in data[2].iterrows():
                                for index2, row2 in data[3].iterrows():
                                    if index == index2:
                                        name = row[1]
                                        salary = row2[6]
                                        proj = row2[7]
                                        dict = {}
                                        dict["name"] = name
                                        dict["salary"] = salary
                                        dict["proj"] = proj
                                        rows_list.append(dict)


                            print(pd.DataFrame(rows_list))
                            # data = pd.DataFrame(data)
                            # print(data.columns)
                            # for index, row in data.iterrows():
                            #     print(row)
                            # print(html)
                            # soup = BeautifulSoup(html, 'lxml')
                            # a = soup.find_all('td')
                            # a = soup.find_all('a', class_="fav-player")

                            # print(a)
                            # response = urllib.request.urlopen(req, context=context)
                            #
                            # soup = BeautifulSoup(response, "html.parser")
                            # table_div = soup.find_all("div", {"class": "k-grid-content k-auto-scrollable"})
                            # print(table_div)

                            # html = response.read()
                            # print(html)
                            # data = pd.read_html(html)   # error thrown No tables found

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

