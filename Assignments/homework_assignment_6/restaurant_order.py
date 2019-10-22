#FLei Shi
#Student 0985491
#Due Date 10/20/2019
#MSITM 6341

#Assignment 6

# Define menu dictionary
menu_dictionary = {
    'Tacos': 5.9,
    'Chips': 2.9,
    'Salsa': 3.4,
    'Quesadilla': 6.9,
    'Burrito': 6.9,
    'Fajita': 10.0
    }

# Initialize customer order
customer_order = ['Tacos', 'Guacamole', 'Burrito']


total_price = 0 # Inital order total is 0
for item in customer_order:
   if item in menu_dictionary.keys():
       print(item.title() + ': ' + '${:,.1f}'.format(menu_dictionary[item]))
       total_price = total_price + menu_dictionary[item] #Cummulatively add to order total if order item is in menu
   else:
       print('We do not have ' + item.title() + '.')
print('---------------\n Order Total: '+ '${:,.1f}'.format(total_price))