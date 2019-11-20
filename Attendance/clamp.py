def clamp(value, min, max):
    min_val = float(min)
    max_val = float(max)
    if value < min_val:
        return(min_val)
    elif value > max_val:
        return(max_val)
    else:
        return(value)
        
print('Value above max:')
print(clamp(1000.1, 10.1, 101.1))

print('Value below min:')
print(clamp(-1000.1, 10.1, 101.1))

print('Value between min and max:')
print(clamp(100, 10.1, 101.1))