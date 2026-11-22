# See README.md for instructions on what to do this program

import random

random.seed(123890)
'''
This sets the seed that random uses
As a result of this when the seed is set to be the same there will be the same outputs
'''
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)