import random



choice = input ("Roll the dice? Y/N:").lower()
while True:
    if choice == 'y':
        dies = random.randint(1,6)
        dies2 = random.randint(1,6)
        print(f"{dies}.{dies2}")
    elif choice == 'n':
        print("TRY LATER")
        break
    else:
        choice = input ("Roll the dice? Y/N:").lower()
        print("WRONG ATTEMPT")