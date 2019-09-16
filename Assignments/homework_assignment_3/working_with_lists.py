# Lei Shi
# 0985491
# 9/15/2019
# MSITM 6341

# Assignment 3


grocery_items = ["apple", "banana", "carrot", "dill", "eggplant"]

prices = [1.99, 0.64, 1.00, 0.50, 1.49]

# 1. Print the 3rd item followed by it’s price
print(grocery_items[2] +": " + '${:,.2f}'.format(prices[2]))

# 2. Print the last item followed by it’s price
print(grocery_items[-1] +": " + '${:,.2f}'.format(prices[-1]))

# 3. Add a 6th item and it’s price
grocery_items.append("fish")
prices.append(8.99)

# 4. Print the list of items
print(grocery_items)

# 5. Print the list of prices
print(prices)

# 6. Remove the first item and it’s price
del grocery_items[0]
del prices[0]

# 7. Double the price of the 2nd item
prices[1] = prices[1]*2

# 8. Print the list of items
print(grocery_items)

# 9. Print the list of prices
print(prices)
