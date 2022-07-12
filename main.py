import mysql.connector
import psycopg2
import sqlite3
import time
import matplotlib.pyplot as plt

queris_SQLite = [int(i) for i in range(1, 23)]
time_SQLite = []

queris_PostgreSQL = [int(i) for i in range(1, 23)]
time_PostgreSQL = []

queris_MySQL = [int(i) for i in range(1, 23)]
time_MySQL = []

for i in ['MySQL']:
    if i == 'SQLite':
        print("Starting SQLite Queries: \n")
        connection = sqlite3.connect('tpch.db')
        curr = connection.cursor()

        fd = open('tpch queries sqlite.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')
        query = 1

        for command in sqlCommands[0:22]:
            try:
                start_time = time.time()
                curr.execute(command)
                end_time = time.time()
                delta_time = end_time-start_time
                time_SQLite.append(delta_time)
                print("Query " + str(query) + " Time Taken: " + str(delta_time) + " seconds")
                query += 1
            except sqlite3.OperationalError as msg:
                print("Command skipped: ", msg)

        connection.close()
    elif i == 'PostgreSQL':
        print("Starting PostgreSQL Queries: \n")
        connection = psycopg2.connect(
            database="tpch", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
        )
        curr = connection.cursor()

        fd = open('tpch queries postgres.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')
        query = 1

        for command in sqlCommands[0:22]:
            try:
                start_time = time.time()
                curr.execute(command)
                end_time = time.time()
                delta_time = end_time-start_time
                time_PostgreSQL.append(delta_time)
                print("Query " + str(query) + " Time Taken: " + str(delta_time) + " seconds")
                query += 1
            except:
                print("error!")

        connection.close()
    elif i == 'MySQL':
        print("Starting MySQL Queries: \n")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="tpch"
        )

        curr = connection.cursor()

        fd = open('tpch queries postgres.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        sqlCommands = sqlFile.split(';')
        query = 1

        for command in sqlCommands[0:22]:
            start_time = time.time()
            curr.execute(command)
            end_time = time.time()
            delta_time = end_time-start_time
            time_MySQL.append(delta_time)
            print("Query " + str(query) + " Time Taken: " + str(delta_time) + " seconds")
            query += 1

        connection.close()

print("\n\n\n\n\n")
print("Times Arrays: ")
print(time_SQLite)
print(time_PostgreSQL)
print(time_MySQL)

plt.plot(queris_SQLite, time_SQLite, label = "SQLite")
plt.plot(queris_PostgreSQL, time_PostgreSQL, label = "PostgreSQL")
plt.plot(queris_MySQL, time_MySQL, label = "MySQL")

plt.xlabel('Queries')
plt.ylabel('Time (sec)')
plt.title('Time vs Queries')
plt.xticks(queris_PostgreSQL)
plt.legend()
plt.show()

'''
Starting SQLite Queries:

Query 1 Time Taken: 6.3058295249938965 seconds
Query 2 Time Taken: 2.67461895942688 seconds
Query 3 Time Taken: 5.8790764808654785 seconds
Query 4 Time Taken: 0.7236552238464355 seconds
Query 5 Time Taken: 4.123389959335327 seconds
Query 6 Time Taken: 1.23903226852417 seconds
Query 7 Time Taken: 6.798696517944336 seconds
Query 8 Time Taken: 13.73497748374939 seconds
Query 9 Time Taken: 38.54736256599426 seconds
Query 10 Time Taken: 1.7958307266235352 seconds
Query 11 Time Taken: 0.815349817276001 seconds
Query 12 Time Taken: 1.3301267623901367 seconds
Query 13 Time Taken: 34.7786648273468 seconds
Query 14 Time Taken: 1.7108283042907715 seconds
Query 15 Time Taken: 2.706150531768799 seconds
Query 16 Time Taken: 0.34880852699279785 seconds
Query 17 Time Taken: 5241.221168041229 seconds
Query 18 Time Taken: 1.5725305080413818 seconds
Query 19 Time Taken: 2.1058266162872314 seconds
Query 20 Time Taken: 7274.275936365128 seconds
Query 21 Time Taken: 10.788492918014526 seconds
Query 22 Time Taken: 782.3217658996582 seconds

Starting PostgreSQL Queries: 
Query 1 Time Taken: 2.0018324851989746 seconds
Query 2 Time Taken: 0.7953236103057861 seconds
Query 3 Time Taken: 1.1171095371246338 seconds
Query 4 Time Taken: 0.3427248001098633 seconds
Query 5 Time Taken: 0.4148991107940674 seconds
Query 6 Time Taken: 0.39522409439086914 seconds
Query 7 Time Taken: 0.47043561935424805 seconds
Query 8 Time Taken: 0.6945817470550537 seconds
Query 9 Time Taken: 1.418503761291504 seconds
Query 10 Time Taken: 0.6632030010223389 seconds
Query 11 Time Taken: 0.17365694046020508 seconds
Query 12 Time Taken: 0.6204557418823242 seconds
Query 13 Time Taken: 0.7750928401947021 seconds
Query 14 Time Taken: 0.41449952125549316 seconds
Query 15 Time Taken: 0.46239542961120605 seconds
Query 16 Time Taken: 0.45548105239868164 seconds
Query 17 Time Taken: 3831.5540685653687 seconds
Query 18 Time Taken: 2.141671895980835 seconds
Query 19 Time Taken: 0.5173454284667969 seconds
Query 20 Time Taken: 20199.45454478264 seconds
Query 21 Time Taken: 1.668536901473999 seconds
Query 22 Time Taken: 0.8826391696929932 seconds

Starting MySQL Queries: 
Query 1 Time Taken: 18.128294467926025 seconds
Query 2 Time Taken: 0.3948788642883301 seconds
Query 3 Time Taken: 83.94888925552368 seconds
Query 4 Time Taken: 6.187437057495117 seconds
Query 5 Time Taken: 15.559936046600342 seconds
Query 6 Time Taken: 2.746222734451294 seconds
Query 7 Time Taken: 25.50528383255005 seconds
Query 8 Time Taken: 63.82933235168457 seconds
Query 9 Time Taken: 143.14844608306885 seconds
Query 10 Time Taken: 11.208197116851807 seconds
Query 11 Time Taken: 7.685924053192139 seconds
Query 12 Time Taken: 6.151596307754517 seconds
Query 13 Time Taken: 241.1137444972992 seconds
Query 14 Time Taken: 9.059811353683472 seconds
Query 15 Time Taken: 3.163893222808838 seconds
Query 16 Time Taken: 4.054150104522705 seconds
Query 17 Time Taken: 3.182103395462036 seconds
Query 18 Time Taken: 3.843073606491089 seconds
Query 19 Time Taken: 2.9517951011657715 seconds
Query 20 Time Taken: 12.97677755355835 seconds
Query 21 Time Taken: 16.267157554626465 seconds
Query 22 Time Taken: 0.7035477161407471 seconds
'''

'''
[6.3058295249938965, 2.67461895942688, 5.8790764808654785, 0.7236552238464355, 4.123389959335327, 1.23903226852417, 6.798696517944336, 13.73497748374939, 38.54736256599426, 1.7958307266235352, 0.815349817276001, 1.3301267623901367, 34.7786648273468, 1.7108283042907715, 2.706150531768799, 0.34880852699279785, 5241.221168041229, 1.5725305080413818, 2.1058266162872314, 7274.275936365128, 10.788492918014526, 782.3217658996582]
[2.0018324851989746, 0.7953236103057861, 1.1171095371246338, 0.3427248001098633, 0.4148991107940674, 0.39522409439086914, 0.47043561935424805, 0.6945817470550537, 1.418503761291504, 0.6632030010223389, 0.17365694046020508, 0.6204557418823242, 0.7750928401947021, 0.41449952125549316, 0.46239542961120605, 0.45548105239868164, 3831.5540685653687, 2.141671895980835, 0.5173454284667969, 20199.45454478264, 1.668536901473999, 0.8826391696929932]
[18.128294467926025, 0.3948788642883301, 83.94888925552368, 6.187437057495117, 15.559936046600342, 2.746222734451294, 25.50528383255005, 63.82933235168457, 143.14844608306885, 11.208197116851807, 7.685924053192139, 6.151596307754517, 241.1137444972992, 9.059811353683472, 3.163893222808838, 4.054150104522705, 3.182103395462036, 3.843073606491089, 2.9517951011657715, 12.97677755355835, 16.267157554626465, 0.7035477161407471]
'''
