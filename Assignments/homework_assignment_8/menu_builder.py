#Lei Shi
#Student 0985491
#Due Date 11/03/2019
#MSITM 6341


# Initiate menu dictionary
menu_items = {}

def ask_user_for_menu_item_name():
#   -This function should prompt the user for “Item Name” and return the result.
    item_name = input("Item Name: ")
    return item_name

def ask_user_for_menu_item_cost():
#    -This function should prompt the user for “Item Cost” and return the result.
    cost = input("Item Cost: ")
    return cost

def add_menu_item(menu):
#    -This function should take as arguments the menu(dictionary), name of the item, and cost of the item
#    -It should then add the item to the menu, displaying a WARNING message if the item already exists

    print("\n-----------------------------------------"
        + "\nPlease enter the menu items for the Restaurant"
        + "\n-----------------------------------------"
        )

    should_ask_for_item = True
    
    while should_ask_for_item:
        item_name = ask_user_for_menu_item_name()
        cost = ask_user_for_menu_item_cost()
        
        if item_name in menu:
            print("WARNING: Item exists")
        else:
            menu[item_name] = cost

        continue_or_not = input("Continue(Y/N)? ")

        if continue_or_not == "N":
            should_ask_for_item = False
            
    print("-----------------------------------------"
        + "\nRestaurant Menu"
        + "\n-----------------------------------------"
        )
    
    for item_name, cost in menu.items():
        print("Item Name: " + item_name + " Cost: " + "{0:.1f}".format(float(cost)))
    print("-----------------------------------------")

add_menu_item(menu = menu_items)

