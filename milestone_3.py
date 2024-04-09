import random

word_list = ['apple', 'banana', 'orange', 'grape', 'strawberry']

word = random.choice(word_list)

def main():
    
    guess = ask_for_input()

    check_guess(guess)
            
def ask_for_input():
    
    while True:
        
        guess = input("Enter guess: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Oops, that's not a valid input")
            
            
def check_guess(letter):
    if letter in word:
        print(f"Good guess! {letter} is in the word")
    else:
        print(f"Sorry, {letter} is not in the word. Try again")
        
if __name__ == "__main__":
    main()