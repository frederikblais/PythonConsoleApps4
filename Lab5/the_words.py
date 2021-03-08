# Ask the user to enter a word, and if the 
# word has already been entered the script will 
# display "The value has already been entered." 
# otherwise it will display "New value 
# registered." and proceed to keep it.

# --> If the word “Show" is entered your program will display the word list at this moment. 

line = '------------------------------------------'
title = '|              Word Logger               |'

# Header
print (line)
print (title)
print (line)

# Create list of words
words = []

input_word = ""

# Check if the word is in the list.
def checkList(word, words):
    if input_word in words:
        print("The value has already been entered.")
        print()
    elif input_word == 'show':
        print(words)
        print()
    else:
        print("New value registered.")
        print()

        # Append the input to the list
        words += [input_word]

while input_word != "show":
    # Ask for input of input_word
    input_word = input('Enter a Word: ')

    checkList(input_word, words)