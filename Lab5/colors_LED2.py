import random

# Header
line = '------------------------------------------'
title = '|              colors_LED2               |'

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
        Blues += [RGB_Value]

    elif RGB_Value in range(-29,-10,1):
        # Append the RGB_Value to the list
        Greens += [RGB_Value]

    elif RGB_Value in range(-9,10,1):
        # Append the RGB_Value to the list
        Yellows += [RGB_Value]

    elif RGB_Value in range(11,30,1):
        # Append the RGB_Value to the list
        Oranges += [RGB_Value]

    elif RGB_Value in range(31,50,1):
        # Append the RGB_Value to the list
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