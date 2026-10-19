def even_integers(value):
    even = []
    for i in range(2,value,2):
        even.append(i)
    return even

print(f"Even integers between 0 and num is: {even_integers((int(input("Enter a number: "))))}")