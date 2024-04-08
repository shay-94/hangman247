import random
import string

word_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']

word = random.choice(word_list)

guess = input("Enter guess: ").lower()

if len(guess) == 1 and guess in string.ascii_lowercase:
    print('Good guess')
    print(word, f'Your guess was: {guess}')
else:
    print("Oops that's not a valid input")
