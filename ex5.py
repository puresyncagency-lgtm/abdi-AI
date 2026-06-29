# importing the random library
import random
problemo = 0
fault = 0
shida = 0
# opening the output in a .txt file
file_path = "file.txt"
with open(file_path, "w") as file:
# excuting the for loop
 for i in range (0,11):
    problemo = 0
    fault = 0
    shida = 0
    sen1 = random.randint(0,25)
    sen2 = random.randint(0,25)
    sen3 = random.randint(0,25)
    if sen1 > 15:
        problemo = problemo + 1
    if sen2 > 15:
        fault = fault + 1
    if sen3 > 15:
        shida = shida + 1
    if problemo + fault + shida >= 2:
# writing the output in the .txt file created   
     file.write(f"FAULT CONFIRMED:{sen1}A,{sen2}A and {sen3}A \n")
    else:
         file.write(f"FALSE ALARM:{sen1}A,{sen2}A and {sen3}A \n")