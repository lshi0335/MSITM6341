a = '101'
b = '11'

def comp_str(x='', y = ''):
    x_num = float(x)
    y_num = float(y)
    print('x=' + x + '; ' + 'y=' + y)
    if x_num == y_num:
        print('x = y')
    elif x_num > y_num:
        print('x > y')
    else:
        print('x < y')

comp_str(a,b)
comp_str('2.236','3.1415926535')
comp_str(a,'101')