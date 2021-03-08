import random

# Header
line = '------------------------------------------'
title = '|              colors_LED3               |'

print (line)
print (title)
print (line)

# Lists
Blues = []
Greens = []
Yellows = []
Oranges = []
Reds = []

# For loop thap executes 10 times
for i in range(100):
    RGB_Value = (random.randint (-50, 50))

    if RGB_Value in range(-50,-30,1):
        # Append the RGB_Value to the list
        if RGB_Value not in Blues:
            Blues += [RGB_Value]

    elif RGB_Value in range(-29,-10,1):
        # Append the RGB_Value to the list
        if RGB_Value not in Greens:
            Greens += [RGB_Value]

    elif RGB_Value in range(-9,10,1):
        # Append the RGB_Value to the list
        if RGB_Value not in Yellows:
            Yellows += [RGB_Value]

    elif RGB_Value in range(11,30,1):
        # Append the RGB_Value to the list
        if RGB_Value not in Oranges:
            Oranges += [RGB_Value]

    elif RGB_Value in range(31,50,1):
        # Append the RGB_Value to the list
        if RGB_Value not in Reds:
            Reds += [RGB_Value]
        

print()
print('Blue')
print('Content: ',Blues)
print()
print('Green')
print('Content: ',Greens)
print()
print('Yellow')
print('Content: ',Yellows)
print()
print('Orange')
print('Content: ',Oranges)
print()
print('Red')
print('Content: ',Reds)
print()