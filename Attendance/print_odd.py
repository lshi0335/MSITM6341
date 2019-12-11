#Lei Shi
#Student 0985491
#Due Date 10/29/2019
#MSITM 6341
#Problem of the Day 

# Create a list of numbers chosen randomly(by yourself) 
# and write a loop to point the elements started at odd index locations


# Import random number library
import random

# Generate a list for random numbers
Rand_List = []

num_elements = 10

random.seed(1022) # set random seed so that result is replicatable

for num in range(num_elements):
    x = random.randint(0,100)
    Rand_List.append(x)

# Print odd indexed elements

print("\nThe random number list is: ")
print(Rand_List)
print("\nThe odd-indexed elements are:")
for idx in range(len(Rand_List)):
    if idx%2==1:
        print(str(Rand_List[idx]) + " Index: ", str(idx))