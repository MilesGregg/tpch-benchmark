import math
import time
import psutil
  
percents = []
start_time = time.time()
while time.time() - start_time < 5:
    percents.append(psutil.cpu_percent(interval=5))

print(percents)
print(max(percents))
print(sum(percents) / len(percents))
