from optimizer import Data
from optimizer import Optimizer



def main():
    position_counts = [1, 2, 3, 1, 1, 1, 1]
    weeks = [3]
    years = [2016]
    budget = 60000

    obj = Optimizer(position_counts, weeks, years, budget)


main()