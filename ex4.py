import random
total = 0
faults = 0
file_path = "fault_log.txt"
with open(file_path, "w") as file:

 for i in range(20):
    no = random.randint(0,25)
    total = total + 1
    if no <= 15:
        file.write(f"{no}A = normal \n")
    elif no > 15:
        file.write(f"{no}A = abnormal \n")
        faults = faults + 1
 file.write(f"total readings = {total} \n")     
 file.write(f"the number of faults = {faults} \n")
 file.write(f"the fault percentage = {faults/total * 100}% \n")