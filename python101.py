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
    guesses_left = 5
    print "\nI'm thinking of a number between 1-10"

    while not_guessed:

        print "You have %d guesses to get it right\n" % (guesses_left)

        guess = raw_input("Pick a number: ")
        if int(guess) == random_number:
            print "You got it!"
            not_guessed = False
    
        else:
            if int(guess) > random_number:
                print guess, 'is too high!\n'
            else:
                print guess, 'is too low!\n'
            number_of_guesses += 1
            guesses_left -= 1

        if number_of_guesses >= 5:
            print "You lose, number of guesses exceeded!"
            not_guessed = False
    
    again = raw_input("Play again (Y/N)?")
    if again == 'N':
        print 'Exiting game.'
        break


