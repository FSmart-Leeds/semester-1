# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

list = read_numbers()
list.sort()

try:                    # will throw error if list is empty as list[0] wont exist
    list[0]
except:
    exit("Error: no numbers provided")

minimum = min(list)
maximum = max(list)

total = sum(list)
amount = len(list)
mean = total / amount

midpoint = amount // 2
if amount % 2 == 0:
    median = (list[midpoint] + list[midpoint - 1]) / 2
else:
    median = list[round(midpoint)]

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median)

