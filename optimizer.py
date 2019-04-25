import numpy as np
import pandas as pd

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
        position_filter = self.data["pos"] == position
        position_data = self.data[position_filter]

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
        raw_data = self._readData() #Read data in from database
        processed_data = self._preprocess(raw_data, weeks, years) #Get only the relevant data we want to work with
        self.data = Data(processed_data, self.positions) #Build data object for our data to separate data by position.

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
        Output: All of the raw data from the database.
        """
        print("Read from database")
        data = pd.DataFrame()

        return data

    def _preprocess(self, raw_data, weeks, years):
        #Return the filtered data, based on the week and year range requested.
        #Aggregate data over the time period for each player. Average over games? Or total?
        
        #TODO:sort the data then return it. How? need data sorted by position AND by points. Separate by 
        #position? Have a class for data, have one dataframe/2Darray for each position and sort those?
        #Have dictionary mapping from position to the sorted data for that position?
        year_filter = raw_data['year'].isin(years)
        data_yearfiltered = raw_data[year_filter]

        week_filter = raw_data['week'].isin(weeks)
        data = data_yearfiltered[week_filter]

        return data

    def knapsack(self):
        #Return the optimal lineup when we consider player salaries
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
                name = self.data.data_all[position][i]
                points = self.data.data_all[position][i]

                max_lineup.append( (position, name, points) ) #Append a tuple of information


        return max_lineup

            
            

        

