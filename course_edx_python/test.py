def pay_1(min_rate,interest_rate,debt,time_pay):
    total =0
    remain_balance=0
    for i in range(time_pay):
        monthly_interest_rate = interest_rate/time_pay
        min_month_pay = debt*min_rate
        monthly_unpaid = debt - min_month_pay
        remain_balance = monthly_unpaid*(monthly_interest_rate+1)
        total+=min_month_pay
        debt = remain_balance
        print('Month:%d\n'%i+'Minimum monthly payment:%.2f\n'%min_month_pay +'Remaining balance:%.2f'%remain_balance )

    print('Total paid:%.2f\n'%total+'Remaining balance:%.2f'%remain_balance)


#pay1(0.02,0.18,5000,12)

def pay_2(interestrate,debt):
    pay =10
    remain =debt
    while remain>0:
        remain = debt
        pay+=10
        for i in range(12):
            month_rate = interestrate/12
            unpaid = remain-pay
            remain = unpaid*(1+month_rate)
    print('lowest payment:%d'%pay)

#pay_2(0.2,4773)

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    if stop - start<=step:
        return f(start)*(stop-start)
    else:
        return f(start)*step+radiationExposure(start+step,stop,step)


#print(radiationExposure(0,11,1))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise'''
    result=[]
    if len(secretWord)==0:
        return False
    for i in secretWord:
        if i in lettersGuessed:
            result.append(True)
        else:
            result.append(False)
    if sum(result)==len(result):
        return  True
    else:
        return  False

def isWordGuessed_1(secretWord, lettersGuessed):
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
        return  True and isWordGuessed_1(secretWord[1:],lettersGuessed)
    else:
        return False


print(isWordGuessed('apple',['a', 'l', 'k', 'p', 'e', 's'] ))

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

#print(getGuessedWord('apple',['e', 'i', 'k', 'p', 'r', 's'] ))


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
print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    def __eq__(self,other):
        return  self.x==other.x and self.y==other.y


    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'


#素数生成器
# Note that our solution makes use of the for/else clause, which
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last








