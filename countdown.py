import time
import random

def main():
    number = random.randint(1,10)
    countdown_to_new_year(number)

def countdown(x):
    for i in range (x):
        print(x - i)
        time.sleep(1)


def countdown_to_new_year(x):
    countdown(x)
    print("Happy New Year!")

main()