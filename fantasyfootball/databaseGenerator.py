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


def main():

    conn = sqlite3.connect("players.db")  # connect to database
    cur = conn.cursor()  # cursor allows sql command execution
    # df = pd.read_pickle("./weeklyDataYears/1970/1970week1Passing.pkl")
    # pd.options.display.max_columns = 4000
    # print (df.iloc[0])  #iloc() is used to select rows
    # print(len(df.index))   #num rows

    # schema(PRIMARY_KEY:recordID(int), playerID(int), name(string), year(int), week(int), pos(int), comp(int),
    # passYards(int), passTD(int), int(int), fum(int), receptions(int), recYards(int), recTD(int), rushYards(int),
    # rushTD(int), proj(int), salary(int))
    sql_create_table = """ CREATE TABLE IF NOT EXISTS players (recordID integer PRIMARY KEY, playerID integer, name text, year integer,
                            week integer, pos integer, comp integer, passYards integer, passTD integer, int integer, fum integer,
                            receptions integer, recYards integer, recTD integer,
                            rushYards integer, rushTD integer,
                            proj integer,salary integer);"""

    cur.execute(sql_create_table)   # create table

    for i in range(1970, 2019):     # for each year
        for j in range(1, 18):      # for each week
            df = pd.read_pickle("./weeklyDataYears/"+str(i)+"/"+str(i)+"week"+str(j)+"Passing.pkl")
            for k in range(len(df.index)):
                if not(checkRow(df.iloc[k]['Name'], i, j)):
                    insert(df.iloc[k], i, j, cur, 'pass')

            df = pd.read_pickle("./weeklyDataYears/"+str(i)+"/"+str(i)+"week"+str(j)+"Receiving.pkl")
            for k in range(len(df.index)):
                if checkRow(df.iloc[k]['Name'], i, j):
                    update(df.iloc[k], i, j, cur,'rec')
                else:
                    insert(df.iloc[k], i, j, cur, 'rec')

            df = pd.read_pickle("./weeklyDataYears/"+str(i)+"/"+str(i)+"week"+str(j)+"Rushing.pkl")
            for k in range(len(df.index)):
                if checkRow(df.iloc[k]['Name'], i, j):
                    update(df.iloc[k], i, j, cur, 'rush')
                else:
                    insert(df.iloc[k], i, j, cur, 'rush')

    conn.commit()
    conn.close()


main()
