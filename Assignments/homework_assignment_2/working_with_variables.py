# Lei Shi
# 0985491
# MSITM6341
# 9/8/2019

# Assignment 2
stock_symbol = "DIS" # The tick symbol for The Walt Disney Company
price = 139.55 # Closing price on 9/5/2019
price_change = 0.71 # Change in closing price from 9/5/2019 to 9/6/2019

print("Symbol: " + stock_symbol.upper() + ", Price: " + str(price) + ", Change: " + str(price_change) + "\n\n")

print("Symbol: " + stock_symbol.lower() + ", Price: " + '${:,.2f}'.format(price) + ", Change: " + str(price_change) + "\n\n")

print("Symbol: " + stock_symbol.upper() + " --- Yesterday's Price: " + str(price - price_change))