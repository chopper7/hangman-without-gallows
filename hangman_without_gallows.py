'''  
[ ALL OF THIS SHOULD BE IN A "README.md" FILE ]

Hangman Part 2: The Game  (15 points possible)

[from "p3-5-Hangman-2.py]

Now you will implement the function hangman, which takes one parameter:
the secretWord the user is to guess.

This starts up an interactive game of Hangman between the user and the computer.
Be sure to take advantage of the three helper functions, (isWordGuessed, 
getGuessedWord, getAvailableLetters) that you defined in the previous part.

There are four important pieces of information you may wish to store:
    secretWord:      The word to guess.
    lettersGuessed:  The letters that have been guessed so far.
    mistakesMade:    The number of incorrect guesses made so far.
    availableLetters:  The letters that may still be guessed. Every time a
          player guesses a letter, the guessed letter must be removed from
          availableLetters (and if they guess a letter that is not in
          availableLetters, you should print a message telling them they've
          already guessed that - so try again!).

* At start of game, let user know how many letters the secretWord contains.
* Ask user to supply one guess (i.e. letter) per round. Your function should
  include calls to raw_input to get the user's guess.
* User should receive feedback immediately after each guess about whether
  their guess appears in the computer's word.
* After each round, you should also display to the user the partially
  guessed word so far, as well as letters that the user has not yet guessed.

Note that if you choose to use the helper functions, you do not need to paste
your definitions in the box. We've supplied our implementations of these
functions for your use in this part of the problem. If you use additional
helper functions, you need to paste the definitions here.

Hints:
    (1) You should start by noticing where we're using the provided functions
      (at the top of ps3_hangman.py) to load the words and pick a random one.
      Note that the functions loadWords and chooseWord should only be used on
      your local machine, not in the tutor. When you enter in your solution in
    the tutor, you only need to give your hangman function.
    (2) Consider using lower() to convert user input to lower case. For example
        guess = 'A'
        guessInLowerCase = guess.lower()
    (3) Consider writing additional helper functions if you need them!
'''

## Observations, thoughts, notes
# This is really more like "Wheel Of Fortune" than Hangman, because we're not
# displaying the gallows and stick figure, just placeholders for the letters.
# I refactored loadWords() to get it running (Py 2 vs 3?)

#######################################################################

## MITx Grader's Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"  # a long string of words separated by spaces

def loadWords():
    '''Returns a list of valid words. Words are strings of lowercase letters.
    Depending on size of word list, function may take a while to finish'''
    #inFile = open(WORDLIST_FILENAME, 'r', 0)
    #line = inFile.readline()                  # line: string
    #wordlist = string.split(line)
    with open(WORDLIST_FILENAME, 'r') as inFile:
        print("Loading word list from file....\n")
        wordlist = inFile.readline().split(' ')
        #print("{} words loaded.".format(len(wordlist)))
    return wordlist

def chooseWord(wordlist):
    '''wordlist (list): list of words (strings)
    Returns a word from wordlist at random'''
    return random.choice(wordlist)


## My helper functions

def isWordGuessed(secretWord, lettersGuessed):
    '''secretWord: contiguous string, the word the user is trying to guess.
    lettersGuessed: list of letters that have been guessed thus far.
    Return True if all letters used in secretWord are in lettersGuessed,
    which means the secretWord has been solved; or False otherwise.
    '''
    for ltr in set(secretWord):
        if ltr not in lettersGuessed:
            return False
        else:
            continue
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''Return a string of letters and underscores representing how
    much of the secret word has been guessed so far.
    secretWord: string, the word the user is trying to guess
    lettersGuessed: list, letters have been guessed so far
    '''
    guessedWord = ""
    for ltr in secretWord:
        if ltr in lettersGuessed:
            guessedWord += ltr
        else:
            guessedWord += "*"
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''Return a string comprised of letters that haven't yet been guessed.
    lettersGuessed: list of letters guessed so far.
    '''
    availableLetters = ""
    for ltr in string.ascii_lowercase:
        if ltr in lettersGuessed:
            continue
        else:
            availableLetters += ltr
    return availableLetters 

##---------------------------------------------------------------------

## Play a game

def hangman(secretWord):
    ''' secretWord: string, the secret word to guess.
     Runs an interactive game of Hangman.
    '''
    guess = ""
    lettersGuessed = []
    mistakes = 8
    #isWordGuessed = False
    
    print('Welcome to the game "Hangman of Fortune!"\n')
    print("""I have a word that is {} letters long. \n
        There's a placeholder for each missing letter, like this: \n
        {} \n
        If you can guess all the letters in the word, you win. \n
        But there's a catch: you can guess just 1 letter at a time. \n
        If your letter is in the word, I'll show it to you. If it's not in 
        the word, it counts against you. \n
        You're only allowed to make 8 wrong guesses, then you lose! \n
        -------------------------------\n
        """.format(len(secretWord), getGuessedWord(secretWord, lettersGuessed)))
    
    while not isWordGuessed(secretWord, lettersGuessed):
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        print("The Secret Word:\n{}".format(guessedWord))
        
        if mistakes > 0:
            print("Available letters: {}\n".format(
                  getAvailableLetters(lettersGuessed)))
            guess = input("Please guess a letter: ").lower()
            lettersGuessed.append(guess)
            #Provide feedback immediately after each guess;
            if guess in secretWord:
                print("Good guess!\n-------------------------------\n")
            else:
                mistakes -= 1
                print("Oops! The letter {} is not in the word.\n".format(guess))
                print("You have {} free mistakes left.\n".format(mistakes))
        else:
            print("You lose! The word was '{}'".format(secretWord))
            quit()
        
    print("The word is '{}'. You win!".format(secretWord))


# Get a randomly-chosen secret word
secretWord = chooseWord(loadWords())

# Start up an interactive game
hangman(secretWord)
