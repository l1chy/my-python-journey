print("It's time to warm up a little bit \U0001F603")
print('-'*10)
number = float(input("Enter a number: "))
check = number % 2
guess = (input(f"Is {number} even or odd? \U0001F914: ")).lower()

if (check==0 and guess=="even") or (check!=0 and guess=="odd"):
    print("Bravooo, thats right! \U0001F973")
elif not guess in ("odd","even"):
    print(f"Sorry I don't understand {guess} \U0001F440")
else:
    print("Sorry, thats a wrong answer \U0001F641")