"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Frederick William Smart
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.

try:
    input = int(input("How much do you want to save every month? "))
except:                 # will catch the error that gets thrown when a the user doesn't enter a number
    print("Invalid amount")
    exit()

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
proj_sav = input*12
print("Projected savings for the year:", proj_sav)

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

proj_sav_and_interest = proj_sav + proj_sav * 0.008
proj_sav_and_interest = "£"+str(round(proj_sav_and_interest,2))       # rounds to 2 d.p then converts to string then adds £ to the front
after_decimal = False
digits_after_decimal = 0
for item in proj_sav_and_interest:
    if after_decimal == True:
        digits_after_decimal += 1
    if item == '.':
        after_decimal = True

if digits_after_decimal == 1:
    proj_sav_and_interest = proj_sav_and_interest+"0"
elif digits_after_decimal == 0:
    proj_sav_and_interest = proj_sav_and_interest+".00"

print("Projected savings for the year with interest:", proj_sav_and_interest)