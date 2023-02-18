from random import  randint
for x in range(1,6):
    guessNumber=int(input("Enter your guess between 1 to 10:"))
    randomNumber = randint(1,20)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("you have lost")
        print("randomNumber was :",randomNumber)