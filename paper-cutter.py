import random

praveen = ('r', 'p', 's')

emoji = {'r': '🪨', 'p': '🧻', 's': '✂️' }

user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").lower()

if user_input not in praveen:
    print("INVALID CHOICES")

computer_choices = random.choice(praveen)


print(f"USER CHOICE {emoji[user_input]}")
print (f"CHOCIES {emoji[computer_choices]}")


if user_input == computer_choices:
    print("TIE")
elif user_input != computer_choices:
    print("win")
else:
    print("TRY LATER")


