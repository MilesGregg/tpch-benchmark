import mysql.connector
import time

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="tpch"
)

curr = connection.cursor(buffered=False)

fd = open('tpch queries postgres.sql', 'r')
sqlFile = fd.read()
fd.close()

sqlCommands = sqlFile.split(';')
query = 1

for command in sqlCommands:
   start_time = time.time()
   curr.execute(command)
   end_time = time.time()
   print("Query " + str(query) + " Time Taken:", end_time-start_time)
   query += 1

connection.close()
