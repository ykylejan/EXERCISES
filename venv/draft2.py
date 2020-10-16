import random

# for i in range(6):
#     for j in range(i):
#         print("*", end="")
#     print()

##
# 8.2 Create a Guess the Number Game in Python using a While loop.
# The computer will think of a random number from 1 to 100, and ask the user to guess it.
# The program will tell if each guess is too high or too low. The player wins if the number is guessed within 5 tries.
#
# • Define a random_number with randit between 0-100.
# • Initialize tries to 5. Let the user keep guessing so long as guesses left is greater than zero.
# • Ask the user for their guess.
# • If they guess correctly, print 'You win!' and break. Decrement guesses left by one. Else, print "You lose!"


RANDOM_NUMBER = random.randint(0,100)
correctNumber = RANDOM_NUMBER

attempt = 5

while attempt > 0:
    userGuess = int(input("Guess a number: "))
    attempt = attempt - 1

    if userGuess < 0 or userGuess > 100:
        print("Error, guess a number from 0-100 only")
    else:
        if userGuess == correctNumber:
            print("You win!")
            break
        else:
            print("Wrong,", attempt, "attempts left")
            if userGuess < correctNumber:
                print("Go higher")
            elif userGuess > correctNumber:
                print("Go lower")
            print("")

        if attempt == 0:
            print("You lose! The correct number is", correctNumber)








