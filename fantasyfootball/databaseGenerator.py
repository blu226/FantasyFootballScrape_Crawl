import pandas as pd
import sqlite3


playerGames = []
players = []
recordID = 0


def checkRow(name, year, week):

    if name not in players:
        players.append(name)

    checkString = name+str(year)+str(week)
    if checkString in playerGames:
        return True
    else:
        return False


def insert(dfRow, year, week, cur, role):
    global recordID
    if year < 2001:
        fg = "FGM"
        xp = "XPM"
    else:
        fg = "FG Made"
        xp = "XP Made"

    if role is 'pass':

        sql_insert_passRow = ('INSERT INTO players (recordID, playerID, name, year, week, pos, comp, passYards, passTD, int, fum) '
                              'VALUES ('+str(recordID)+', '+str(players.index(dfRow['Name']))+', ?, '
                              ''+str(year)+', '+str(week)+', ?, '+str(dfRow['Comp'])+', '+str(dfRow['Yds'])+', '
                              ''+str(dfRow['TD'])+', '+str(dfRow['Int'])+', '+str(dfRow['FUM'])+')')

        cur.execute(sql_insert_passRow, (dfRow['Name'], dfRow['pos']))

    elif role is 'rec':
        sql_insert_recRow = ('INSERT INTO players (recordID, playerID, name, year, week, pos, receptions, recYards, recTD, fum) '
                             'VALUES ('+str(recordID)+', '+str(players.index(dfRow['Name']))+', ?, '
                             ''+str(year)+', '+str(week)+', ?, '+str(dfRow['Rec'])+', '+str(dfRow['Yds'])+', '
                             ''+str(dfRow['TD'])+','+str(dfRow['FUM'])+')')
                             # """+dfRow['proj']+""","""+dfRow['salary']+""")"""

        cur.execute(sql_insert_recRow, (dfRow['Name'], dfRow['pos']))

    elif role is 'rush':
        sql_insert_rushRow = ('INSERT INTO players (recordID, playerID, name, year, week, pos, rushYards, rushTD, fum) '
                              'VALUES ('+str(recordID)+', '+str(players.index(dfRow['Name']))+', ?, '
                              ''+str(year)+', '+str(week)+' , ?, '+str(dfRow['Yds'])+', '+str(dfRow['TD'])+', '+str(dfRow['FUM'])+')')
                              # """ + dfRow['proj'] + """,""" + dfRow['salary'] + """)"""

        cur.execute(sql_insert_rushRow, (dfRow['Name'], dfRow['pos']))

    elif role is 'def':
        sql_insert_defRow = ('INSERT INTO players (recordID, playerID, name, year, week, pos, defInt, pa, sacks)'
                             'VALUES ('+str(recordID)+', '+str(players.index(dfRow['Name']))+', ?, '
                             ''+str(year)+', '+str(week)+', ?, '+str(dfRow['INT'])+', '+str(dfRow['PA'])+', '
                             ''+str(dfRow['Sacks'])+')')

        cur.execute(sql_insert_defRow, (dfRow['Name'], 'D'))

    elif role is 'kick':
        sql_insert_kickRow = ('INSERT INTO players (recordID, playerID, name, year, week, pos, fgm, fga, xpm, xpa)'
                              'VALUES ('+str(recordID)+', '+str(players.index(dfRow['Name']))+', ?, '
                              ''+str(year)+', '+str(week)+', ?, '+str(dfRow[fg])+', '+str(dfRow['FG Att'])+', '
                              ''+str(dfRow[xp])+', '+str(dfRow['XP Att'])+')')

        cur.execute(sql_insert_kickRow, (dfRow['Name'], 'K'))

    recordID += 1
    print(recordID)


def update(dfRow, year, week, cur, role):

    # Rec: add receptions, recYards, recTD
    if role is 'rec':
        sql_update_recRow = ('UPDATE players '
                             'SET receptions = '+str(dfRow['Rec'])+', recYards = '+str(dfRow['Yds'])+', recTD = '+str(dfRow['TD'])+' '
                             'WHERE name = ? AND year = '+str(year)+' AND week = '+str(week)+')')
        cur.execute(sql_update_recRow, (dfRow['Name']))

    # Rush: add rushYards, rushTD
    elif role is 'rush':
        sql_update_rushRow = ('UPDATE players '
                              'SET rushYards = '+str(dfRow['Yds'])+', rushTD = '+str(dfRow['TD'])+' '
                              'WHERE name = ? AND year = '+str(year)+' AND week = '+str(week)+')')
        cur.execute(sql_update_rushRow, (dfRow['Name']))
    else:
        print("uh oh")


def processPickle(cur, year, week, type, role):
    df = pd.read_pickle("./Data/" + str(year) + "/week_" + str(week) + "/"+type+".pkl")
    for k in range(len(df.index)):
        t = df.iloc[k]['Name']
        if not isinstance(t, float):
            if checkRow(df.iloc[k]['Name'], year, week):
                update(df.iloc[k], year, week, cur, role)
            else:
                insert(df.iloc[k], year, week, cur, role)
        else:
            print("NaN")


def main():

    conn = sqlite3.connect("players.db")  # connect to database
    cur = conn.cursor()  # cursor allows sql command execution
    #df = pd.read_pickle("./Data/2001/week_1/Defense.pkl")
    #pd.options.display.max_columns = 4000
    #print(df)  # iloc() is used to select rows

    # schema(PRIMARY_KEY:recordID(int), playerID(int), name(string), year(int), week(int), pos(int), comp(int),
    # passYards(int), passTD(int), int(int), fum(int), receptions(int), recYards(int), recTD(int), rushYards(int),
    # rushTD(int), fgm(int), fga(int), xpm(int), xpa(int), defInt(int), pa(int), sacks(int), proj(int), salary(int))
    sql_create_table = """ CREATE TABLE IF NOT EXISTS players (recordID integer PRIMARY KEY, playerID integer, name text, year integer,
                            week integer, pos integer, comp integer, passYards integer, passTD integer, int integer, fum integer,
                            receptions integer, recYards integer, recTD integer,
                            rushYards integer, rushTD integer,
                            fgm integer, fga integer, xpm integer, xpa integer,
                            defInt integer, pa integer, sacks integer, 
                            proj integer,salary integer);"""

    cur.execute(sql_create_table)   # create table

    for i in range(1970, 2019):     # for each year
        for j in range(1, 18):      # for each week
            processPickle(cur, i, j, "Passing", "pass")
            processPickle(cur, i, j, "Receiving", "rec")
            processPickle(cur, i, j, "Rushing", "rush")
            processPickle(cur, i, j, "Defense", "def")
            processPickle(cur, i, j, "Placekick", "kick")
            conn.commit()

    conn.commit()
    conn.close()


main()
