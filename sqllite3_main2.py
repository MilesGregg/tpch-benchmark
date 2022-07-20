import sqlite3
import threading
import time
import psutil

def run_diagnostics(query):
    t = threading.currentThread()
    percents_cpu = []
    percents_ram = []
    while getattr(t, "do_run", True):
        percents_cpu.append(psutil.cpu_percent(interval=0.001, percpu=False))
        percents_ram.append(psutil.virtual_memory()[2])
    print("Query " + str(query) + " Diagonstics:")
    print("   - Average CPU Usage:", sum(percents_cpu) / len(percents_cpu))
    print("   - Average RAM Usage:", sum(percents_ram) / len(percents_ram))

connection = sqlite3.connect('tpch.db')
curr = connection.cursor()

fd = open('tpch queries sqlite.sql', 'r')
sqlFile = fd.read()
fd.close()

sqlCommands = sqlFile.split(';')
query = 1

for command in sqlCommands[0:22]:
    try:
        t = threading.Thread(target=run_diagnostics, args=(query,)) #args=("task",)
        t.start()
        start_time = time.time()
        curr.execute(command)
        end_time = time.time()
        print("\nQuery " + str(query) + " Time Taken:", end_time-start_time)
        query += 1
        t.do_run = False
        t.join()
    except sqlite3.OperationalError as msg:
        print("Command skipped: ", msg)

connection.close()
