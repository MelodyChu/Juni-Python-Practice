# Have the computer pick a random number between 1-100.
# Ask the user to guess the number. Keep asking until the user guesses correctly.
# Tell the user to guess lower or higher after each incorrect guess.
# Bonus: Start the user with 8 guesses. After each guess, tell the user how many guesses are remaining. End the game if the user runs out of guesses.

import random # import function
computer_guess = random.randint(0, 100) # define computer guess
user_guess = input("Guess a number between 1 & 100!") # define user guess
user_guess = int() # convert user guess into integer


for i in range(0,9): # loop to check user_guess
    if user_guess == computer_guess: # if user guesses correctly they win
        print ("You win!")
        return 
    elif user_guess < computer_guess: # if user guesses lower than computer guess; prompt another guess. but needs to return to top of loop
        print ("Guess higher!")
        guess_higher = input("Guess a higher number!")
        guess_higher=int()
    elif user_guess > computer_guess:
        print ("Guess lower!")
        guess_lower = input("Guess a lower number!")
        guess_lower =int()
    
        

