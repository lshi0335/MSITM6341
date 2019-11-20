def clamp(value, min, max):
    # Force value, min, and max to float in case they are strings.
    value_f = float(value)
    min_val = float(min)
    max_val = float(max)
    if value_f < min_val:
        clamp_val = min_val
        print('Value ' + str(value) + ' is below min. ' + str(min) + ' and clamped to: ' + str(clamp_val))
    elif value_f > max_val:
        clamp_val = max_val
        print('Value ' + str(value) + ' is above max. ' + str(max) + ' and clamped to: ' + str(clamp_val))
    else:
        clamp_val = value_f
        print('Value ' + str(value) + ' is between min. ' + str(min) + ' and max. ' + str(max) + ', and remained: ' + str(clamp_val))
    return(clamp_val)  

print(clamp(1000.1, 10.1, 101.1))

print(clamp(-1000.1, 10.1, 101.1))

print(clamp(100, 10.1, 101.1))

print(clamp('100', 10.1, '101.1'))