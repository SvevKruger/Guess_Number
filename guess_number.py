import random

def guess_number():
    guess_number = 0
    random_number = random.randint(1, 20)
    while guess_number != random_number:
        guess_number = int(input("Insert a number between 1 and 20 "))
        if guess_number > random_number:
            print("Your number is too high")
        elif guess_number < random_number:
            print("Your number is too low")
    if guess_number == random_number:
        print(f"Congrats, that's right. The correct number is {guess_number}")

guess_number()
