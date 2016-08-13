import random
secret=random.randint(1,10)
print("工作室")
temp = input("猜我心里想的那个数字：")
guess = int(temp)
while (guess !=secret):
    temp = input("猜错了，请重新输入")
    guess = int(temp)
    if guess ==secret:
        print("卧槽这都猜对了")
        print("猜对了也没奖励！" )                     
    else:
        if guess>secret:
            print("大了")
        else:
            print("小了")
print("游戏结束，不玩啦……" )         
