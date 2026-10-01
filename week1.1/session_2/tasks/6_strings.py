# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")
# this makes all of the chars in the string lowercase
print(f"Modified String 2: {user_string.upper()}")
# this makes all of the chars in the string uppercase
print(f"Modified String 3: {user_string.strip()}")
# this removes empty characters before and after the string 
print(f"Modified String 4: {user_string.replace('a', '@')}")
# replaces all instances of a with an @
print(f"Modified String 5: {user_string.capitalize()}")
# sets the first character in a string to uppercase
print(f"Modified String 6: {user_string[::-1]}")
# reverses the order of the chars in a string 
print(f"Modified String 7: {user_string.title()}")
# puts an uppercase char at the start of every word in the string
print(f"Modified String 8: {len(user_string)}")
# returns the length of the string - amount of chars in it
print(f"Modified String 9: {user_string.find('a')}")
# returns the index of the first 'a'
print(f"Modified String 10: {user_string.count('a')}")
# counts how many chars in the string is 'a'
print(f"Modified String 11: {user_string.startswith('Hello')}")
# returns true if the string starts with 'hello' false if not
print(f"Modified String 12: {user_string.endswith('!')}")
# returns true if the string ends with '!' false if not
print(f"Modified String 13: {user_string.isalnum()}")
# returns true if the string consists of only numbers and letters false if not
print(f"Modified String 14: {user_string.isalpha()}")
# returns true if every char in the string is an alphabetical character false if not
print(f"Modified String 15: {user_string.isdigit()}")
# returns true if all chars in the string are numbers


######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!