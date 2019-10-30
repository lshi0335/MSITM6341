#Lei Shi
#Student 0985491
#Due Date 10/29/2019
#MSITM 6341
#Problem of the Day 1

# Import random number library
import random

# Generate a list for random numbers
Rand_List = []

num_elements = 10

random.seed(1022) # set random seed so that result is replicatable

for num in range(num_elements):
    x = random.randint(0,100)
    Rand_List.append(x)

print(str(num_elements) +" random integers are generated: ")
print(Rand_List)

# Use function to find largest

# Largest = max(Rand_List)

# Use loop to find largest

idx = 0
for x in Rand_List:
    if idx == 0:
        Largest = Rand_List[idx]
    elif Rand_List[idx] >= Rand_List[idx-1]:
        Largest = Rand_List[idx]
    idx = idx + 1

print("\nThe largest element is: " + str(Largest))