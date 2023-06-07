#do not change any function names
def findAlphabeticallyFirstWord(string):
    #start your code here
    all_words = string.split()

    w = all_words[0]

    # loop through all words from the first word
    for word in all_words:
        if word < w:
            w = word
    
    return w

#Ask the user for the input string, separated by a space or comma
string = input("Enter the string: ")

# Find the first word in alphabetical order
first_word = findAlphabeticallyFirstWord(string)

# Print the result
print(first_word)
