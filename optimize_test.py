from optimizer import Data
from optimizer import Optimizer



def main():
    position_counts = [1, 2, 3, 1, 1, 1, 1]
    weeks = [3]
    years = [2018]
    budget = 60000

    print()
    obj = Optimizer(position_counts, weeks, years, budget)
    lineup = obj.knapsack()
    print("Knapsack:", lineup)
    print()
    max_lineup = obj.maxLineup()
    print("Max Lineup:", max_lineup)
    print()


main()