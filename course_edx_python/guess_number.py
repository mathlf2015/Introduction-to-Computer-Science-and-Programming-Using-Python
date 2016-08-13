#二分法猜数字
def guess_number():
    number =int(input('Please think of a number between 0 and 100:'))
    low = 0
    high = 100
    ans = (low+high)/2
    while True:
        print('is your number %s?'%ans)
        result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly:")
        if result not in ['l','h','c']:
            print('Sorry, I did not understand your input.')
        elif result=='l':
            low = ans
            ans = (low+high)/2
        elif result=='h':
            high = ans
            ans = (low+high)/2
        else :
            print('bingo')
            break
    print('your number is:%s'%ans)

def guess_sqr():
    number =float(input('please input a number:'))
    low = 0
    high = number
    ans = (low+high)/2
    while abs(ans**2-number)>0.01 and ans < number:
        if ans**2>number:
            high = ans
            ans =(low+high)/2
        else:
            low =ans
            ans =(low+high)/2
    print('your number is:%s'%ans)
#牛顿迭代法
def get_result():
    low = 1
    number = float(input('please input a number:'))
    ans = (low+number)/2
    while abs(ans**4 + ans -number)>=0.01:
        ans = ans - (ans**4 + ans -number)/(4*ans**3+1)
        print(ans)
    print('the result is:%s'%ans)








if __name__=='__main__':
    get_result()
    #guess_number()
    #guess_sqr()
