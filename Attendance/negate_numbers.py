#Lei Shi
#Student 0985491
#Due Date 10/29/2019
#MSITM 6341
#Problem of the Day 2

# Import random number library
import random

# Generate a list for random numbers
Rand_List = []

num_elements = 10

random.seed(1023) # set random seed so that result is replicatable

for num in range(num_elements):
    x = random.randint(0,100)
    Rand_List.append(x)

print(str(num_elements) +" random integers are generated: ")
print(Rand_List)

# Use loop to negate all
Negate_List = [-x for x in Rand_List]

print("Negated list is: ")
print(Negate_List)