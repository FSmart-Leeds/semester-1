# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv
with open("sales.csv") as s:
    contents = s.readlines()

date = []
product = []
sales_amount = []
units_sold = []
region = []
for line in contents:
    if line == contents[0]:
        continue
    data = line.split(",")
    date.append(data[0])
    product.append(data[1])
    sales_amount.append(int(data[2]))
    units_sold.append(int(data[3]))
    region.append(data[4])



# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
print("The highest sale is", max(sales_amount))
print("The total sales is", sum(units_sold))
print("The average sale amount is", (sum(units_sold) / len(units_sold)))
print("The most sold item is", product[units_sold.index(max(units_sold))])

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows