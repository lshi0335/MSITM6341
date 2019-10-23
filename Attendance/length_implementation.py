grocery_items = ['Apples', 'Oranges', 'Pineapple']

print("Length of grocery_items is " + str(len(grocery_items)))

# Alternative way to find out length of a list 
Length = sum(1 for x in grocery_items)

print("Length found in an alternative way is " + str(Length))