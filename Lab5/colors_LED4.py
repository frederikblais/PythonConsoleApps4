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

# Counters
Count_Blue = 0
Count_Green = 0
Count_Yellow = 0
Count_Orange = 0
Count_Red = 0

# For loop thap executes 10 times
for i in range(100):
    RGB_Value = (random.randint (-50, 50))

    if RGB_Value in range(-50,-30,1):
        # Append the RGB_Value to the list, increase counter
        if RGB_Value not in Blues:
            Blues += [RGB_Value]
            Count_Blue += 1

    elif RGB_Value in range(-29,-10,1):
        # Append the RGB_Value to the list, increase counter
        if RGB_Value not in Greens:
            Greens += [RGB_Value]
            Count_Green += 1

    elif RGB_Value in range(-9,10,1):
        # Append the RGB_Value to the list, increase counter
        if RGB_Value not in Yellows:
            Yellows += [RGB_Value]
            Count_Yellow += 1

    elif RGB_Value in range(11,30,1):
        # Append the RGB_Value to the list, increase counter
        if RGB_Value not in Oranges:
            Oranges += [RGB_Value]
            Count_Orange += 1

    elif RGB_Value in range(31,50,1):
        # Append the RGB_Value to the list, increase counter
        if RGB_Value not in Reds:
            Reds += [RGB_Value]
            Count_Red += 1
        

print()
print('Blue was generated',Count_Blue, 'times.')
print('Content: ',Blues)
print()
print('Green was generated',Count_Green, 'times.')
print('Content: ',Greens)
print()
print('Yellow was generated',Count_Yellow, 'times.')
print('Content: ',Yellows)
print()
print('Orange was generated',Count_Orange, 'times.')
print('Content: ',Oranges)
print()
print('Red was generated',Count_Red, 'times.')
print('Content: ',Reds)
print()