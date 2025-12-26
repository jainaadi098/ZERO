import time
import random

print("In this game we will count the number from 1 \n And at the place of numbers multiple of 5 we count 0 ")
print("Let start the game!")


def process(count,num):
    if (count+1)%5==0 and num==0:
        return True
    elif (count+1)%5!=0 and num==(count+1):
        return True
    else:
        return False

def play():
    player=1
    computer=2
    turn=random.randint(1,2)
    count=0
    while True:
        if turn==1:
            time.sleep(1)
            print("Player Turn")
            num=int(input("Enter :"))
            valid=process(count,num)
            if valid==False:
                
                break
            else:
                count+=1
                turn=2
        if turn==2:
            time.sleep(1)
            print("Computer Turn")
            if (count+1)%5==0:
                num=0
                count+=1
                
            else:
                num=count+1
                count+=1
            time.sleep(1.5)
            print(num)
            turn=1

play()
print("Game Over")