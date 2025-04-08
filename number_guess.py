import random

number_guess = random.randint(1, 100)

while True:
    try:
        number = int(input("ENTER THE NUMBER: "))
        if number_guess > number:
            print("NUMBER IS HIGH")
        elif number_guess < number:
            print("NUMBER IS LOW")
        else:
            print("CORRECT! YOU GUESSED IT.")
            break  # exit the loop when guessed correctly
    except ValueError:
        print("NUMBER IS INVALID. PLEASE ENTER A VALID INTEGER.")
