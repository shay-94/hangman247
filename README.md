# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Add your list of words to the play_game() function call on line 57 and run the python file in your terminal window then follow the prompts. Good luck!

File Structure:

The program is broken into multiple functions, the 'main' function encapsulates the other functions and is what we call to run the program.
The other functions are:

ask_for_input() - asks the user for their guess and ensures that it isn't a number or special character. Calls check_guess function and updates the 
                word_list variable that stores the '_''s that are displayed to the player with their correct guesses

check_guess() -   checks the guessed letter to see if it is in the word, returns a string telling the user whether they were correct or not.
                It also updates the number of lives counter and the number of letters left to guess counter.

play_game() - the main function that contains the loop for the game while checking whether the player has won or lost all their lives


*NOTE* 

I've added some extra functionality outside the given scope of the project. I've added a play_again() function that asks the player if they want to play again and
if they do, resets the game. I've also added diagrams for the stages of the hangmans fate as you play the game.