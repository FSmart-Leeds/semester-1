# Week 1.5, Session 2: Task 5
from data import Dataset
# Write a program here to create a Dataset containing data
# from a file named by the user
d = Dataset("test.data")
# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
print(len(d))
print(d.mean())
print(d.median())
for v in d:
    print(v)