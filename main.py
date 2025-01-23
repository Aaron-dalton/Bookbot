

# This is the main function of the bookbot
def main():
    # Setting up the code to open the text and return different data
    try:
        with open(input("Enter the path of the file you wish to read: "), 'r') as f: # Opening the users input file
            file_contents = f.read()
            # Telling the user the word count
            lettercount = letter_counting(file_contents)
            word_counting(file_contents)
            dict_sorting(lettercount)
    except FileNotFoundError:
        print("That file does not exist")
        main()

# Setting up the function to count the amount of words
def word_counting(file_contents):
    word_count = file_contents.split()
    print(f"There are {len(word_count)} words in this document")

# Setting up letter counter function
def letter_counting(file_contents):
    
        lettercount = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0, 
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
        }
        lowercase_file = file_contents.lower()
        for letter in lowercase_file: # Setting up the loop to count the letters
            if letter in lettercount: # Checking if the letter is in the dictionary
                lettercount[letter] += 1
        return lettercount

# Setting up the function to sort the dictionary
def dict_sorting(lettercount):
    lettercount_tuple = list(lettercount.items()) # Converting the dictionary to a list
    sorted_lettercount = sorted(lettercount_tuple, key=lambda x: x[1], reverse=True) # Sorting the list
    sorted_lettercount = dict(sorted_lettercount) # Converting the list back to a dictionary
    print(f"Sorted letter count: {sorted_lettercount}")
# Calling the function
main()