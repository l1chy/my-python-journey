import time
import random

words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into',
'could',
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like',
'then',
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find',
'also',
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through',
'long',
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because',
'good',
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world',
'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show',
'house', 'both',
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
'move', 'thing',
'general', 'school', 'never', 'same', 'another', 'begin', 'while',
'number', 'part',
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child',
'small', 'since',
'against', 'late', 'home', 'interest', 'large', 'person', 'open',
'public', 'follow',
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern',
'around',
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead',
'system',
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]

# Index targeting and manual list reversal.

word_index = random.randint(0, len(words) - 1)
word = words[word_index].strip().lower()
lst_word = list(word)
lst_word.reverse()
reversed_word = ''.join(lst_word)

# During development, I discovered a more Pythonic, concise way to achieve this:
#  word = random.choice(words).strip().lower()
#  reversed_word = word[::-1]
# I kept the explicit list method active here to showcase manual data manipulation.
# ==============================================================================

# The game begins and the time taken to answer is calculated

print(f"Welcome to the reversed word game!\n-------\nThe reversed word is: {reversed_word}\n-------")
time_before = time.time()
answer = input("The word is: ")
time_taken = time.time() - time_before

# ==============================================================================
# Originally, I used 'elif answer == word and time_taken > 5'.
# I refactored this into a nested 'if' to remove redundant string comparison checks,
# making the code cleaner and easier to maintain.
# ==============================================================================
if answer == word:
    if time_taken <= 5:
        print(f"You won! You took {time_taken:.2f} seconds!")
    else:
        print(f"Correct answer BUT You took {time_taken:.2f} seconds. (MAX IS 5!)")
else:
    print(f"You lost! Correct word was '{word}'")