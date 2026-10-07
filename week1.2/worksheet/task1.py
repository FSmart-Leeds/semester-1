# Worksheet 1.2: Task 1 Solution
import sys

try:
    input = int(input("Enter an integer between 0 - 100: "))
    if input > 100 or input < 0:
        raise()
except:
    exit("Error: Grade must be an integer between 0 and 100")

if input < 40:
    print(input, "is a Fail")
elif input < 70:
    print(input, "is a Pass")
else:
    print(input, "is a Distinction") 
