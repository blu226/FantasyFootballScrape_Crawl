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
from selenium.common.exceptions import WebDriverException
import os
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

        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options, )

        for season in range(2015, 2019):
            print("SEASON:", season)
            for team in range(0, 32):
                print("TEAM:", team)
                for position in range(2, 8):
                    for week in range(1, 18):
                        path_to_folder = "./Data/" + str(season) + "/week_" + str(week) + "/"

                        url_to_crawl = self.url + "position=" + str(position) + "&team=" + str(team) + "&season=" + str(season)
                        url_to_crawl += "&seasontype=1&scope=2&startweek=" + str(week) + "&endweek=" + str(week)

                        try:

                            browser.get(url_to_crawl)
                            html = browser.page_source
                            data = pd.read_html(html)
                            rows_list = []
                            if len(data) > 2:
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

                                new_data = pd.DataFrame(rows_list)

                                if position < 6:
                                    categories = ["Passing", "Rushing", "Receiving"]
                                elif position == 6:
                                    categories = ["Placekick"]
                                else:
                                    categories = ["Defense"]

                                for category in categories:
                                    filename = category + ".pkl"

                                    data = pickle.load(open(path_to_folder + filename, "rb"))
                                    print(data)

                                    # for index, row in data.iterrows():
                                    #     for index2, row2 in new_data.iterrows():
                                    #         if type(row["Name"]) == str and type(row2["name"]) == str:
                                    #             if row["Name"].lower() == row2["name"].lower() and row["proj"] == "null":
                                    #                 row["proj"] = row2["proj"]
                                    #                 row["salary"] = row2["salary"]
                                    #
                                    # pickle.dump(data, open(path_to_folder + filename, "wb"))

                        except (urllib.error.URLError, ValueError, WebDriverException, ConnectionResetError, ConnectionError, TimeoutError, ConnectionRefusedError, socket.timeout) as e:
                            print("ERROR:", e)

        browser.close()


crawl = weeklyCrawler()
crawl.crawl()

