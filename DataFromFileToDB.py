# BigPicture:
#   1. Read data from file.csv
#   2. Write data to Database
# Details:
# Want to transform the data read from the file into tuples.
# FROM Data in Reader object? TO Data in Tuples.
#       FROM Lists TO Tuples
# THEN:
#     Create/ConnectTo database, Create Table, Create Query - Matching Data, Add/Write Data to Table/DB using Query and Data


# Add functionality: 
# Q: Do we want to Write a query for deleting table or records in a table?

import sqlite3 as sqlite
import csv
import os
import sys

dbConnection = sqlite.connect('musicScales.db')
data = []

def readDataFromFile():
    # with open('D:/Software-Development/DataFiles/alexandra-music-scales/data/music_scales.csv', newline='') as csvfile:
    with open(os.path.join(sys.path[0], "music_scales.csv"), "r", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            data.append(tuple(row))
            # print(', '.join(row))
        data.pop(0)

def addDataToTable():
    sql = 'INSERT INTO MUSICSCALES (scale_name, root, column_c, column_d, column_e, column_f) values(?, ?, ?, ?, ?, ?)'

    with dbConnection:
        dbConnection.executemany(sql, data)

def createTable():
    with dbConnection:
        dbConnection.execute("""
            CREATE TABLE MUSICSCALES(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                scale_name  TEXT,
                root        TEXT,
                column_c    INTEGER,
                column_d    INTEGER,
                column_e    INTEGER,
                column_f    INTEGER
            );
        """)

def doAllDbStuff():
    readDataFromFile()
    createTable()
    addDataToTable()

doAllDbStuff()