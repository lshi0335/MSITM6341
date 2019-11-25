#Lei Shi
#Student 0985491
#Due Date 11/24/2019
#MSITM 6341

class Date():
    def __init__(self, dd, mm, yyyy):
        self.day = int(dd)
        self.month = int(mm)
        self.year = int(yyyy)
        # Dictionary for printing month in their names.
        self.month_name = {1:'January', 2:'Feburary', 3:'March', 4:'April', 5:'May', 6:'June', 
                        7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
        # Ensure day and months input are in valid range.
        if (self.day not in list(range(1, 32))) or (self.month not in list(range(1,13))):
            raise ValueError('Oops! Check input value for month and/or day.')
    
    def change_date(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)   
        # Ensure day and months input are in valid range.
        if (self.day not in list(range(1, 32))) or (self.month not in list(range(1,13))):
             raise ValueError('Oops! Check input value for month and/or day.')

    def print_date(self):
        if self.year == '' or self.month=='' or self.day == '':
            print('Error: missing year, month, or day')

        else:
            month_print = self.month_name[self.month]
            print(month_print + ' ' + str(self.day) + ', ' + str(self.year))

# Oject 1
mydate1 = Date(1, 1, 1960)

mydate1.change_date(19, 6, 2019)

mydate1.print_date()

# Object 2

mydate2 = Date(24, 11, 2019)

mydate2.change_date(31, 8, 2019)

mydate2.print_date()