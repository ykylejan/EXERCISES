import random

##
# 8.1 Write a simple calculator program using a While loop.
# Ask the user to input 2 numbers and select an operation: addition, subtraction, division, and multiplication.
# Perform the selected operation and display the output. Ask the user if they want to repeat or enter the letter Q to quit the program.
#

x = True

while x == True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Select an operation (Addition, Subtraction, Multiplication, Division): ")

    # Line 18-26 are the code segments for Addition and loop conditions
    if operation == "Addition":
        numValue = num1 + num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 29-37 are the code segments for Subtraction and loop conditions
    elif operation == "Subtraction":
        numValue = num1 - num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 40-48 are the code segments for Multiplication and loop conditions
    elif operation == "Multiplication":
        numValue = num1 * num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 51-59 are the code segments for Division and loop conditions
    elif operation == "Division":
        numValue = num1 / num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False
print("-" * 180)
##
# 8.2 Create a Guess the Number Game in Python using a While loop.
# The computer will think of a random number from 1 to 100, and ask the user to guess it.
# The program will tell if each guess is too high or too low. The player wins if the number is guessed within 5 tries.
#
# • Define a random_number with randit between 0-100.
# • Initialize tries to 5. Let the user keep guessing so long as guesses left is greater than zero.
# • Ask the user for their guess.
# • If they guess correctly, print 'You win!' and break. Decrement guesses left by one. Else, print "You lose!"

correctNumber = random.randint(0,100)
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
print("-" * 180)
##
# 8.3 Write a FOR loop that prints the first 128 ASCII values followed by the corresponding characters.
# Take note that the ASCII values in the range 0-31 are special control characters with no standard print representation.
# You might see strange symbols in the output for these values.
#
x = range(128)

for n in x:
    print(chr(n), end="")
print()
print("-" * 180)
##
# 8.4 Run a program that will ask the user to input a sentence.
# Filter out the letter 'A' or 'a' from the sentence and replace with 'X'. Then, print the newly formed sentence.
#
sentence = input("Enter a sentence: ")

for letter in sentence:
    if "A" == letter or "a" == letter:
        print("X", end="")
    else:
        print(letter, end="")
