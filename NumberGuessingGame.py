import random
number=random.randint(1,9)
i=0
while(i<5):
    guess=int(input("guess the number"))
    if(guess==number):
        print("congratuations you won!!!")
        break
    elif(guess<number):
        print("your guess is too low!!")
    else:
        print("your guess is too high!")
    i=i+1    

if(i==5):
    print("sorry!you lost the number is",number)

