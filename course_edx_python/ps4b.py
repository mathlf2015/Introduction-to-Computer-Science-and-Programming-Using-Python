from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    score_max = 0
    # Create a new variable to store the best word seen so far (initially None)  
    word_best = None
    # For each word in the wordList
    for each in wordList:
        if isValidWord(each,hand,wordList) and getWordScore(each,n)>score_max:
            score_max = getWordScore(each,n)
            word_best = each
    return  word_best



        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)

            # Find out how much making that word is worth

            # If the score for that word is higher than your best score

                # Update your best score, and best word accordingly


    # return the best word you found.
#print(compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6))

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    displayHand(hand)
    choose_word = compChooseWord(hand,wordList,n)
    score = 0
    while choose_word!=None:
        score+=getWordScore(choose_word,n)
        print('%s earned %s points. Total: %s  points'%(choose_word,getWordScore(choose_word,n),score))
        hand = updateHand(hand,choose_word)
        displayHand(hand)
        choose_word = compChooseWord(hand,wordList,n)

#compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList,n=7):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand =dealHand(n)
    while True:
        message = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        while  message not in ['n','r','e']:
            print('Invalid command')
            message = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if message=='e':
            break
        who_to_play = input('Enter u to have yourself play, c to have the computer play: ')
        while who_to_play not in ['c','u']:
            print('Invalid command')
            who_to_play = input('Enter u to have yourself play, c to have the computer play: ')
        if who_to_play=='c'and message=='n':
            hand =dealHand(n)
            compPlayHand(hand,wordList,n)
        elif who_to_play=='c' and message=='r':
            compPlayHand(hand,wordList,n)
        elif who_to_play=='u'and message=='n':
            hand = dealHand(n)
            playHand(hand,wordList,n)
        elif who_to_play=='u' and message=='r':
            playHand(hand,wordList,n)


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


