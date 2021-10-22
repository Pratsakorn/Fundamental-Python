import random
color = ["red", "green", "blue"]
while True:
    colors=color[random.randint(0,len(color)-1)]
    c=str(input("Guess color : "))
    while True:
        if c.lower() == colors:
            print("CORRECT!!!")
            break
        else:
            c=str(input("Nope, try again : "))
    print("It was fun?")
    again=str(input("Let's play again!!, type 'no' to quit. "))
    if again.lower()=='no':
            break
print("Thank you for playing with me")
