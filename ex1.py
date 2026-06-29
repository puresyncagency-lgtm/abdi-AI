
# asking for the list of current value
total = 0
normal = 0
for i in range(5):
    loo = float(input("what is the current value? "))
    total = total + loo   
    if loo > 15:
        print(f"the current value {loo} amps exceeds the current limit")
    else:
        normal = normal + 1
print(f"the number of normal values is {normal}")
print(f"the average is {total/5} amps")
