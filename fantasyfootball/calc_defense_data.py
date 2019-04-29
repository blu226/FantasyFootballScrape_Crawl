import pandas as pd
import pickle

for season in range(1970, 2019):
    for week in range(1, 18):
        teams = []
        row_list = []

        path_to_data = "./Data/" + str(season) + "/week_" + str(week) + "/Passing.pkl"
        path_to_save = "./Data/" + str(season) + "/week_" + str(week) + "/Defense.pkl"
        data = pickle.load(open(path_to_data, "rb"))

        for index, row in data.iterrows():
            teams.append(row["Team"])

        teams = list(dict.fromkeys(teams))
        for team in teams:
            row_dict = {"Name": team, "PA": 0, "Sacks": 0, "INT": 0, "Salary": "null", "proj": "null"}
            for index, row in data.iterrows():
                opp_team = row["Opp"].strip().split()
                if len(opp_team) == 2:
                    score_row = row["Score"].strip().split()
                    outcome = score_row[0]
                    score = score_row[1].split("-")
                    score = list(map(int, score))
                    if opp_team[1] == team:
                        row_dict["INT"] += int(row["Int"])
                        row_dict["Sacks"] += int(row["Sck"])
                        if outcome == "W":
                            row_dict["PA"] = max(score)
                        else:
                            row_dict["PA"] = min(score)

            row_list.append(row_dict)

        new_data = pd.DataFrame(row_list)
        pickle.dump(new_data, open(path_to_save, "wb"))
