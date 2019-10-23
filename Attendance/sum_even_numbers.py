# Import random number library
import random

# Generate a list for random numbers
Rand_List = []

num_elements = 10

for num in range(num_elements):
    x = random.randint(0,100)
    Rand_List.append(x)

print(str(num_elements) +" random integers are generated: ")
print(Rand_List)

# Pick out even numbers from the random list
Even_Nbr = []

for x in Rand_List:
    if x%2==0:
        Even_Nbr.append(x)

print("\nEven numbers from above list are: ")
print(Even_Nbr)

print("\nSum of all even number is: " + str(sum(Even_Nbr)))
