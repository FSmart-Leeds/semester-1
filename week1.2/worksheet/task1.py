# Worksheet 1.2: Task 1 Solution
try:
    input = int(input("Enter an integer between 0 - 100: "))
    if input > 100 or input < 0:
        raise()
except:
    print("Error: Grade must be an integer between 0 and 100")
    exit()