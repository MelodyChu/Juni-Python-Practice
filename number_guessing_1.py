"""A number-guessing game."""
from random import randint

name = raw_input("Howdy, what's your name? ")
greeting = name + ", I'm thinking of a number between 1 & 100."
print greeting

def number_guessing():
    secret_num = randint(1,100)
    print secret_num

    guess_counter = 1
    score_list = []

    while True:
        try:
            guessed_num = int(raw_input("Guess a number between 1 & 100 "))
            print secret_num # as a check
        except ValueError:
            print "Oops that's not a valid number!"
            continue
        #   pass guessed_num.isstring() == True:
        #   print "Please enter a number"
        if int(guessed_num) <= 0 or guessed_num >= 101:
            print "Please enter a number between 1 and 100"
        elif int(guessed_num) < secret_num:
            print "Your guess is too low!"
        elif int(guessed_num) > secret_num:
            print "Your guess is too high"
        elif int(guessed_num) == secret_num:
            print "Well done, " + name + "! You found my number in " + str(guess_counter) + " tries!"
            score_list.append(guess_counter) #put the first round into score list
            play_again = raw_input("Would you like to play again? Y / N? ")
            if play_again in "Yy": 
                guess_counter = 1 #reset back to 1 every time game restarts
                continue
            else:
                print "Your best score is " + str(min(score_list)) + "! Thanks for playing!"
                break

        guess_counter += 1
    return # guess_counter

number_guessing() #call the function to execute it

"""

play_again = raw_input("Would you like to play again? Y / N? ")
while play_again in "Yy": #
    number_guessing() # call function again
else:
    print "Your best score is " + "! Thanks for playing!"
"""

#Asking user to play again
"""
def replay_game():
    play_again = raw_input("Would you like to play again? Y / N? ")
    while play_again in "Yy": #
        number_guessing()
    else:
        return "Your best score is " + "! Thanks for playing!"
"""
 #calling the function
# replay_game()
        












# Put your code here
