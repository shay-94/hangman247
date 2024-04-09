# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

No installation required, just run the python file in your terminal window and follow the prompts. Good luck!

File Structure:

The program is broken into multiple functions, the 'main' function encapsulates the other functions and is what we call to run the program.
The other functions are:

ask_for_input() - asks the user for their guess and ensures that it isn't a number or special character. Calls check_guess function and updates the 
                word_list variable that stores the '_''s that are displayed to the player with their correct guesses

check_guess() -   checks the guessed letter to see if it is in the word, returns a string telling the user whether they were correct or not.
                It also updates the number of lives counter and the number of letters left to guess counter.


