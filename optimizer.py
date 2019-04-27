import numpy as np
import pandas as pd
import sqlite3

class Data():
    """
    Meant to keep track of separate instances of the same data for ease of use.
    For example, getting the maximum lineup lets us look at each position data individually. This is
    more difficult to do with the single large table of data.
    """
    def __init__(self, data, positions):
        #Build all data into a dictionary, separating data for each position
        self.data = data
        self.data_all = dict()
        self.data_all["ALL"] = data

        #These can be refactored into a loop
        self.data_all["QB"] = self.positionSelector("QB")
        self.data_all["RB"] = self.positionSelector("RB")
        self.data_all["WR"] = self.positionSelector("WR")
        self.data_all["TE"] = self.positionSelector("TE")
        self.data_all["FLEX"] = self.positionSelector("FLEX")
        self.data_all["K"] = self.positionSelector("K")
        self.data_all["D"] = self.positionSelector("D")

    def positionSelector(self, position):
        if position == "FLEX":
            position_filter = self.data["pos"].isin(["RB", "WR", "TE"])

        else:
            position_filter = self.data["pos"] == position

        position_data = self.data[position_filter].reset_index(drop=True)

        return position_data


class Optimizer():
    def __init__(self, 
    position_counts, #Python list of number of each position requested. 
    weeks, #Python list of what weeks are being requested
    years, #Python list of years requested
    budget=None, #The set budget our algorithm has to stay under. Default is none
    ):
        self.positions = ["QB", "RB", "WR", "TE", "FLEX", "K", "D"]

        self.lineup_counts = self._buildLineupCounts(position_counts)
        self.budget = budget

        #"Pretty up" our data we read in. Getting it ready for use
        raw_data = self._readData() #Read data into a dataframe from database.
        processed_data = self._preprocess(raw_data, weeks, years) #Get only the relevant data we want to work with
        self.data = Data(processed_data, self.positions) #Build data object for our data to separate data by position.
        print("Finished setup!")

    def _buildLineupCounts(self, position_counts):
        """
        Input: position_counts - List of counts for each position. This is in the order as shown below. 
        Format: [QB, RB, WR, TE, FLEX, K, D]
        Output: Returns a list like [('QB',num), ('RB',num), WR, TE, FLEX, K, D]
        The list contains a tuple for each position with the number of players for that position requested.
        """
        
        lineup = list()
        for index, num in enumerate(position_counts):
            lineup.append( (self.positions[index], num) )
        return lineup

    def _readData(self):
        """
        Read in the data from our database.
        Output: All of the raw data from the database, in a Pandas Dataframe.
        """
        print("Read from database")
        con = sqlite3.connect("fantasyfootball/players.db")
        data = pd.read_sql_query("select * from players", con)
        con.close()

        return data

    def _preprocess(self, raw_data, weeks, years):
        #Return the filtered data, based on the week and year range requested.
        #Aggregate data over the time period for each player. Average over games? Or total?
        
        #TODO:sort the data then return it. How? need data sorted by position AND by points. Separate by 
        #position? Have a class for data, have one dataframe/2Darray for each position and sort those?
        #Have dictionary mapping from position to the sorted data for that position?
        '''Previous approach. Got Boolean Series Key error
        year_filter = raw_data["year"].isin(years)
        data_yearfiltered = raw_data[year_filter]
       
        week_filter = raw_data["week"]
        week_filter2 = week_filter.isin(weeks) #Split into two lines because was getting "Boolean Series Key will be reindexed to match DataFrame index"
        data = data_yearfiltered[week_filter2]
        '''

        mask = raw_data[['year', 'week']].isin({'year': years, 'week': weeks}).all(axis=1)
        data = raw_data[mask]

        return data

    def knapsack(self):
        #Return the optimal lineup when we consider player salaries
        """
        Need to use: self.budget
        """
        max_lineup = []

        return max_lineup


    def maxLineup(self):
        """
        Return maximum possible lineup
        Returns: Python list of tuples. Each tuple contains (position, player name, points scored)
        """
        max_lineup = []

        
        for position, position_number in self.lineup_counts:
            #For each position, get the top n players based on our lineup numbers

            for i in range(position_number):
                #Get a player for each number of times the user requested for this position.
                #TODO: ACCESS THE DATA AT THIS ROW. DATA IS SORTED SO CAN JUST QUERY THE TOP OF DATA
                print("position:", position)
                print(self.data.data_all[position])
                name = self.data.data_all[position].iloc[i]["name"]
                points = self.data.data_all[position].iloc[i]["proj"]
                salary = self.data.data_all[position].iloc[i]["salary"]

                max_lineup.append( (position, name, points, salary) ) #Append a tuple of information


        return max_lineup

            
        

