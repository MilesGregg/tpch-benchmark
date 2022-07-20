import sqlite3
import time

connection = sqlite3.connect('tpch.db')
curr = connection.cursor()

curr.execute("SELECT COUNT(*) FROM lineitem")

for i in curr.fetchall():
   print(i)

'''fd = open('tpch queries sqlite.sql', 'r')
sqlFile = fd.read()
fd.close()

sqlCommands = sqlFile.split(';')
query = 1

for command in sqlCommands[0:22]:
    try:
        start_time = time.time()
        curr.execute(command)
        end_time = time.time()
        print("Query " + str(query) + " Time Taken:", end_time-start_time)
        query += 1
    except sqlite3.OperationalError as msg:
        print("Command skipped: ", msg)'''

connection.close()
