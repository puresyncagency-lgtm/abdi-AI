# asking the user for the current and voltage values
current = int(input("what is the current value? "))
voltage = int(input("what is the voltage value? "))
# return the evaluation results
if current > 15:
    print(f"the current {current}A indicates an overcurrent fault")
if voltage < 180:
    print(f"the voltage {voltage}V indicates an undervoltage fault")
elif voltage > 250:
    print(f"the voltage {voltage}V indicates an overvoltage fault")
if current <= 15 and voltage in range(180,251):
    print("the system is healthy")
elif current >15 and voltage in range(180,251):
    print()
elif current <=15 and voltage not in range(180,251):
    print("fault in the voltage")
else:
    print("fault in the system")





