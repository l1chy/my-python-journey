import random

print("Guess the coinflip!"+f"\n{'-'*20}"+"\nEnter 1 for heads\nor 2 for tails.\n")

win = random.randint(1,2)
guess = int(input("Enter your choice: "))

if guess == 1 or guess == 2:
    choice = True
else:
    choice = False
    print("Please enter 1 or 2 only.")

if win == 1:
    side = "Heads"
else:
    side = "Tails"

if choice == True:
    if guess == win:
        print(f"Coin is {side}, You win!")
    else:
        print(f"Coin is {side}, You lose!")