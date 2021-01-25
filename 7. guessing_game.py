import random

num = random.randint(1,10)

while True:
    for i in range (3):
        guess = int(input("What is your guess: "))
        if (guess == num):
            print ("correct")
            break
        elif(guess > num):
            print ("too big")
        elif guess < num:
            print ("too small")
    print ("the number is :", num)
    break
