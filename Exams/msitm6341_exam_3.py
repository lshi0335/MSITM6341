# Name: Lei Shi
# Student ID: 0985491
# Due Date: 12/3/2019 10:30 pm
# MSITM 6341

class Rectangle():
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)
    # Ensure width and height input are positive.
        if self.width <= 0 or self.height <= 0:
            raise ValueError('Dimensions should be positive.')

    def print_dimensions(self):
        print("Dimensions of the rectangle is: " + str(self.width) + "x" + str(self.height))
    
    def get_area(self):
        return(self.width*self.height)

    def get_perimeter(self):
        return 2*(self.width+self.height)

# Test code 1
Rectangle_1 = Rectangle(20.5, 50)
Rectangle_1.print_dimensions()
print(Rectangle_1.get_area())
print(Rectangle_1.get_perimeter())

# Test code 2: This should raise error for negative dimension input
#Rectangle_2 = Rectangle(-20, 50)
#Rectangle_2.print_dimensions()
#print(Rectangle_2.get_area())
#print(Rectangle_2.get_perimeter())


# Test code 3: This should raise error for non-numeric dimension input
#Rectangle_3 = Rectangle("a", 50)
#Rectangle_3.print_dimensions()
#print(Rectangle_3.get_area())
#print(Rectangle_3.get_perimeter())




        