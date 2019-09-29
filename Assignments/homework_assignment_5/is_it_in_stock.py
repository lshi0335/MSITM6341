# Lei Shi
# 0985491
# MSITM6341
# 9/29/2019

# Assignment 5

# Initialize lists
menu_items_in_stock = ['Tacos', 'Chips', 'Salsa', 'Quesadilla']
customer_order = ['Tacos', 'Guacamole', 'Burrito', 'Chips', 'Salsa']

# Change all elements in lists to lower case
menu_items_in_stock = [x.lower() for x in menu_items_in_stock]
customer_order = [x.lower() for x in customer_order]

# Check if an item in customer_order is in menu_items_in_stock
for x in customer_order:
    if x in menu_items_in_stock:
        print('We have ' + x.capitalize() + ' in stock.')
    else:
        print('We do not have ' + x.capitalize() + ' in stock.')
