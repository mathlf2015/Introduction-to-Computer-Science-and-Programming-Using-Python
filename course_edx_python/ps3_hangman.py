# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words_1.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("%s"%len(wordlist)+"words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise'''
    if len(secretWord)==0:
        return  False
    elif len(secretWord)==1 and secretWord in lettersGuessed:
        return True
    elif secretWord[0] in lettersGuessed:
        return  True and isWordGuessed(secretWord[1:],lettersGuessed)
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result=''
    for i in secretWord:
        if i in lettersGuessed:
            result+=str(i)
        else:
            result+='_'
    return  result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letter_avail=''
    letter = 'abcdefghijklmnopqrstuvwxyz'
    for i in letter:
        if i not in lettersGuessed:
            letter_avail+=str(i)
        else:
            letter_avail+=''
    return letter_avail
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("I'm thinking of a word shat is %s word long"%len(secretWord))
    guess=[]
    i=0
    while i<8:
        print('You have %s guesses left'%(8-i))
        print('Available letters: %s'%getAvailableLetters(guess))
        guess_letter = input('please  guess a letter:').lower()
        #print(guess)
        if guess_letter in guess:
            print("Oops! You've already guessed that letter:%s"%guessd_word)
        while guess_letter not in guess:
            guess.append(guess_letter)
            guessd_word=getGuessedWord(secretWord,guess)
            if guess_letter in secretWord:
                print('good guess %s'%guessd_word)
            else:
                i+=1
                print('Oops! That letter is not in my word:%s'%guessd_word)
        if isWordGuessed(secretWord,guessd_word):
            print('you win this game')
            break
    print('Sorry, you ran out of guesses. The word was else.')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord ='apple'
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
