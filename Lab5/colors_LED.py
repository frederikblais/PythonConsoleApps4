import random

# Header
line = '------------------------------------------'
title = '|              colors_LED                |'

print (line)
print (title)
print (line)

ranges = (-30, -10, 10, 30)

# For loop thap executes 10 times
for i in range(10):
    RGB_Value = (random.randint (-50, 50))

    if RGB_Value in range(-50,-30,1):
        print(RGB_Value, '\t', 'Blue')
    elif RGB_Value in range(-29,-10,1):
        print(RGB_Value, '\t', 'Green')
    elif RGB_Value in range(-9,10,1):
        print(RGB_Value, '\t', 'Yellow')
    elif RGB_Value in range(11,30,1):
        print(RGB_Value, '\t', 'Orange')
    elif RGB_Value in range(31,50,1):
        print(RGB_Value, '\t', 'Red')        