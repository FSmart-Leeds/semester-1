import random

# Get user to input how many random numbers they want
num = int(input("how many random numbers do you want?: "))
# Generate this many random numbers
nums = []
while num > 0:
    num -= 1
    nums.append(random.randint(0,100))
# Write the random numbers to a file named random.txt, one number per line
f = open("random.txt",'w')
print(*nums,sep="\n" ,file=f)