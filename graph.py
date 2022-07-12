import random
import matplotlib.pyplot as plt

queris_SQLite = [int(i) for i in range(1, 23)]
time_SQLite = [random.randint(0, 100) for _ in range(1, 23)]
plt.plot(queris_SQLite, time_SQLite, label = "SQLite")
  
queris_PostgreSQL = [int(i) for i in range(1, 23)]
time_PostgreSQL = [random.randint(0, 100) for _ in range(1, 23)]
plt.plot(queris_PostgreSQL, time_PostgreSQL, label = "PostgreSQL")

queris_MySQL = [int(i) for i in range(1, 23)]
time_MySQL = [random.randint(0, 100) for _ in range(1, 23)]
plt.plot(queris_MySQL, time_MySQL, label = "MySQL")

plt.xlabel('Queries')
plt.ylabel('Time (sec)')
plt.title('Two lines on same graph!')
plt.xticks(queris_PostgreSQL)
plt.legend()
plt.show()
