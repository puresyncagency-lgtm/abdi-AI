# importing the CSV module
import csv
import random
minute = 0
# opening the CSV file
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
 writer = csv.writer(file) 
 writer.writerow(["Minute", "current", "status" ])
# starting the random generation of current values
 for i in range(1,1441):
    current = random.randint(0,25)
    minute = minute + 1
    if current > 15:
      status = "abnormal"
    else:
      status = "normal"
    writer.writerow([minute, current, status])