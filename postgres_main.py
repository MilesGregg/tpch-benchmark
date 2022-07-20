import psycopg2
import time

connection = psycopg2.connect(
   database="tpch", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
curr = connection.cursor()

curr.execute("SELECT COUNT(*) FROM lineitem")

for i in curr.fetchall():
   print(i)

'''fd = open('tpch queries postgres.sql', 'r')
sqlFile = fd.read()
fd.close()

sqlCommands = sqlFile.split(';')
query = 1

for command in sqlCommands[0:22]:
   start_time = time.time()
   #curr.execute(command)
   end_time = time.time()
   print("Query " + str(query) + " Time Taken:", end_time-start_time)
   query += 1'''

connection.close()

