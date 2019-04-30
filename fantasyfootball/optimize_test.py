from optimizer import Data
from optimizer import Optimizer
import numpy as np



def main():
    position_counts = [1, 2, 3, 1, 1, 1, 1]
    weeks = [3]
    years = [2015]
    budget = 60000

    print()
    obj = Optimizer(position_counts, weeks, years, budget)
    lineup = obj.knapsack()
    print("Knapsack:", lineup)
    print()

    sum = 0
    for tup in lineup:
        money = tup[3]
        if(money is not np.nan):
            print("type", type(money))
            print("How much:", money)
            sum += money

    print("Spent this much money:", sum)    
    print("With this much budget:", budget)


    max_lineup = obj.maxLineup()
    print("Max Lineup:", max_lineup)
    print()


main()