import random


def getGuess():
    guess = raw_input("Enter a guess: ")
    try:
        return int(guess)
    except:
        print "Invalid input. Please input an integer."
        return getGuess()

def desireContinue():
    input = raw_input("Play again? (Y/N): ")
    if input.upper() != "Y" and input.upper() != "N":
        desireContinue()
    elif input.upper() == "N":
        print "\nExiting game. Goodbye!\n"
        return exit()

def main():


    while True:

        random_number = random.randint(1, 10)
        not_guessed = True
        number_of_guesses = 0
        guesses_left = 5
        print "\nI'm thinking of a number between 1 and 10...\n"

        while not_guessed:

            print "Guesses remaining: %d" % (guesses_left)
            guess = getGuess()

            if guess == random_number:
                print "You got it!\n"
                not_guessed = False

            else:
                if guess > random_number:
                    print guess, 'is too high!\n'
                else:
                    print guess, 'is too low!\n'
                number_of_guesses += 1
                guesses_left -= 1

            if number_of_guesses >= 5:
                print "You lose, number of guesses exceeded!\n"
                not_guessed = False

        desireContinue()


main()
