import random
num=input("guess a number from 1 to 100: ")
num2=random.randint(1,100)
if num==num2:
    print("You guessed right, are you a psychic lol")
else:
    print("Aww try again")or("Nuh uh better luck next time")