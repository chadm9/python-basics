import random

# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# if first_name == last_name:
#     print "You first and last names are equal"

# age = raw_input("How old are you: ")

# if int(age) >= 21:
#     print "You can buy beer!"
# else:
#     print "You are underage!"

#random_number = random.randint(1, 10)
#not_guessed = True
#number_of_guesses = 0
#play_again = True
#again = 'T'

while True:
    random_number = random.randint(1, 10)
    not_guessed = True
    number_of_guesses = 0

    while not_guessed:
        guess = raw_input("Guess a number from 1-10: ")
        if int(guess) == random_number:
            print "You got it!"
            not_guessed = False
    
        else:
            if int(guess) > random_number:
                print guess, 'is too high!'
            else:
                print guess, 'is too low!'
            number_of_guesses += 1

        if number_of_guesses >= 5:
            print "You lose, number of guesses exceeded!"
            not_guessed = False
    
    again = raw_input("Play again (Y/N)?")
    if again == 'N':
        break


