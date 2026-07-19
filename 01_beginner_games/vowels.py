vowels = ['A', 'E', 'I', 'O', 'U']
name = input("Enter your name: ")
answer = input(f"Does {name} start with a vowel?: ").lower()
first_ltr = name[0].upper()
print('-'*25)

if (first_ltr in vowels) and (answer=="yes"):
    print(f"Bravo! Thats correct, {name} starts with a vowel.")
elif (first_ltr not in vowels) and (answer=="no"):
    print(f"Bravo! Thats correct, {name} doesn't start with a vowel.")
elif (first_ltr in vowels) and (answer=="no"):
    print("Sorry, wrong answer.. Lets try again!")
elif (first_ltr not in vowels) and (answer=="yes"):
    print("Sorry, wrong answer.. Lets try again!")
else:
    print("Please enter (Yes or No) answers only.")