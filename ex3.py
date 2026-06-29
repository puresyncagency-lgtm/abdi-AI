import random
total = 0
faults = 0
for i in range(20):
    no = random.randint(0,25)
    total = total + 1
    if no <= 15:
        print(f"{no}A = normal")
    elif no > 15:
        print(f"{no}A = abnormal")
        faults = faults + 1
print(f"total readings = {total}")     
print(f"the number of faults = {faults}")
print(f"the fault percentage = {faults/total * 100}%")