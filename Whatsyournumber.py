import time

import math

x = 0
y = 1
min = 0
max = 11
people_max = max - 1
print(f"Start thinking of a intager between {min} and {people_max}, except for 4.")
time.sleep(0)
response = input(f"Is {y} your number? ")
while x == 0:
    
    if y < min:
        y = min + 1
    if y > max:
        y = max - 1

    
    if response == "yes":
        print(f"So {y} is your number!")
        x = 1
    elif response == "higher":
        min = y
        y = y*3
        print(min)
        if y < min:
            y = min + 1
        if y > max:
            y = max - 1
        response = input(f"Is {y} your number? ")
    elif response == "lower":
        max = y
        y = y/2
        print(max)
        if y < min:
            y = min + 1
        if y > max:
            y = max - 1
        response = input(f"Is {y} your number? ")
    if max - min == 1:
        print("Nice try, you can't read directions, making me, the more powerful being. Ha!")
        x = 1
        
    min = math.floor(min)
    max = math.floor(max)
    


