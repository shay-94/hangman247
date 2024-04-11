import random

class Hangman:
    def __init__(self, num_lives, word_list) -> None:
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        #Checks if the guess this round is in the answer word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            self.num_letters -=1
        else:
            print(f"Sorry, {guess} is not in the word. Try again. You have {self.num_lives} lives left")
            self.num_lives -=1
            
    def ask_for_input(self):
    #Gets players guess and checks its a letter and then whether it's correct
        #Asks user for their guess this round
        guess = input("Enter guess: ").lower()
        #Checks if guess is numeral or symbol and whether the player already guessed the letter
        if len(guess) == 1 and guess.isalpha():
            if guess not in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                for count,letter  in enumerate(self.word):
                    if guess == letter:
                        self.word_guessed[count] = letter
                print(self.num_letters, self.word_guessed)
            else:
                print("You already tried that letter!")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    

def play_game(word_list):
    #Main function
    num_lives = 5
    game = Hangman(num_lives, word_list)
    
    while True:
        if game.num_lives == 0:
            print("Sorry, you lose! Please try again")
            break
        elif game.num_letters > 0:
          game.ask_for_input()
        else:
            print("Congratulations! You win!")
            break
    
            

if __name__ == "__main__":
    play_game(['apple', 'banana', 'orange', 'grape', 'strawberry'])