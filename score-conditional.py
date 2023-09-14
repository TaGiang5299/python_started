x = input('score?')
try:
    y = float(x)
except:
    print('error')
    exit()  # Exit the program if there's an error

if y >= 0.0 and y <= 1.0:  # Check if y is in the valid range
    if y >= 0.9:
        print('A')
    elif y >= 0.8:
        print('B')
    elif y >= 0.7:
        print('C')
    elif y >= 0.6:
        print('D')
    else:
        print('F')
else:
    print('Invalid score. Score should be between 0.0 and 1.0')
print('all done')