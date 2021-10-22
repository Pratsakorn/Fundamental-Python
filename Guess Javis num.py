import random
number = random.randint(0,10)
guess = int(input("Can U guess my nub (0-10) ? "))
while True:
    if guess == 5 :
        print("correct!!")
        break
    else :
        guess=int(input("no!!, Try again "))