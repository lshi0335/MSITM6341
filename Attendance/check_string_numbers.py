a = '101'
b = '11'

def comp_str(x='', y = ''):
    print('\nx=' + x + '; ' + 'y=' + y)
    try:       
        x_num = float(x)
        y_num = float(y)
        if x_num == y_num:
            print('x = y')
        elif x_num > y_num:
            print('x > y')
        else:
            print('x < y')
    except ValueError:
        return print('Error: Function comp_str() requires two string (or numeric) inputs.'
                    +'\nPlease make sure that the string input has valid numeric meaning.')

comp_str(a,b)
comp_str('2.236','3.1415926535')
comp_str(a,'101')
comp_str('2.236','pi')
