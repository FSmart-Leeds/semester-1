def listprint(shopping : list):
    for item in shopping:
        print(item, end = " ")
    print()
# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
listprint(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
listprint(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
listprint(shopping)

# Replace bananas with grapes

shopping[shopping.index("bananas")] = "grapes"
listprint(shopping)

# Add yoghurt, just after milk
shopping.insert(shopping.index("milk") + 1, "yogurt")
listprint(shopping)

for item in shopping:
    print(item, end = " ")
print()
