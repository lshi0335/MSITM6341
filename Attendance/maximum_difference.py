def max_diff_int(int_list):
    # Check if all members in the list are integers
    for num in int_list:
        if not num == int(num):          
            print('Error: At least one of the values in the input list is not an integer.')
            quit() # Stop excuting the function if any value in the input list is not an integer

    # Find the maximum, minimum, and the difference between them
    max_int = max(int_list)
    min_int = min(int_list)
    return(int(max_int - min_int))

# Example 1
list_of_int1 = [12, -20.0,3, 1]
print(max_diff_int(list_of_int1))

# Example 2
list_of_int2 = [12.1,-20.0,3, 1]
print(max_diff_int(list_of_int2))