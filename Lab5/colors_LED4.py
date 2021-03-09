import random
from collections import Counter

# Header
line = '------------------------------------------'
title = '|              colors_LED4               |'

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
        # Append the RGB_Value to the list, increase counter
        Blues += [RGB_Value]

    elif RGB_Value in range(-29,-10,1):
        # Append the RGB_Value to the list, increase counter
        Greens += [RGB_Value]

    elif RGB_Value in range(-9,10,1):
        # Append the RGB_Value to the list, increase counter
        Yellows += [RGB_Value]

    elif RGB_Value in range(11,30,1):
        # Append the RGB_Value to the list, increase counter
        Oranges += [RGB_Value]

    elif RGB_Value in range(31,50,1):
        # Append the RGB_Value to the list, increase counter
        Reds += [RGB_Value]
        

print()
print('Blue List:', Counter(Blues))
print()
print('Green List:', Counter(Greens))
print()
print('Yellow List:', Counter(Yellows))
print()
print('Orange List:', Counter(Oranges))
print()
print('Red List:', Counter(Reds))
print()