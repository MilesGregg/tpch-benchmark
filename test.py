'''import math
import time
import psutil
import os
  
percents_cpu = []
percents_ram = []

start_time = time.time()
while time.time() - start_time < 5:
    percents_cpu.append(psutil.cpu_percent(interval=1, percpu=False))
    percents_ram.append(psutil.virtual_memory()[2])

print(percents_cpu)
#print(max(percents))
print(sum(percents_cpu) / len(percents_cpu))
print(sum(percents_ram) / len(percents_ram))'''