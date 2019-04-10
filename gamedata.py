# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:28:24 2019

@author: Anthony
"""


'''
GOAL: 
    Parse every game on the website "www.pro-football-reference.com" we can.
    Get data for every player that played in the game.
    Build a table with information about the game, week, player name, all the player's stats
    
HOW:
    For every year, for every week, scrape the urls of all the games (in the <a href> tag)
    Using that list of urls, scrape all of them
    
    FIGURE OUT DYNAMICALLY HOW MANY WEEKS THERE ARE FOR THAT YEAR
    
NOTES:
    Only up to week 14 in the 1970s
    
    
'''

import numpy as np





class GameCrawler():
    def __init__(self):
        #Set up to crawl game data
        
        base_url = "https://www.pro-football-reference.com"
        num_game_urls = 0 #Number of game urls we have.
        game_urls = [] #The list of urls for each NFL game we want data from.
        
        #Year Information
        start_year = 2018
        end_year = 2018
        years = np.arange(start_year, end_year + 1) #Which years we are interested in. Include the end_year
        
        
    def crawlGames(self):
        #Get the urls for all the games we want to look at.
        
        for year in self.years:
            #For each year, look at the url directory for this year
            year_url = self.base_url + "/years/" + str(year)
            #TODO: FIGURE OUT HOW MANY WEEKS WERE IN THIS YEAR
            
            for week in self.weeks:
                
                #For each week, look within this year, week combo
                
                url = year_url + "/week_" + week + ".htm"                
        
    def crawlEachGame():
        #Crawl every game url that we have collected for its data
        #ASSUMES WE HAVE RUN CRAWLGAMES() FIRST
        