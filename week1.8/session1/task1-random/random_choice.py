import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num = int(input("Enter a number: "))
chosen = random.sample(names, num)
# Display the chosen names, one per line
for choice in chosen:
    print(choice)