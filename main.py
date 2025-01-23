# This is the main function of the bookbot
def main():
    # Setting up the code to open the text and return different data
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = file_contents.split()
        print(f"There are {len(word_count)} words in this document") # Telling the user the word count
        letter_counting(file_contents) # Calling the letter counting function
        word_counting(file_contents) # Calling the word counting function
        
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
            " ": 0
        }
        lowercase_file = file_contents.lower()
        for letter in lowercase_file: # Setting up the loop to count the letters
            if letter in lettercount: # Checking if the letter is in the dictionary
                lettercount[letter] += 1
        # Printing the letter count
        print(f"Letter count: {lettercount}")

# Calling the function
main()