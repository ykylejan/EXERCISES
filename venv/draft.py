import random

# gameList = ["Final Fantasy XV","TEKKEN 7","Hollow Knight","Brawlhalla","Persona 5"]
# i = 1
#
# for item in gameList:
#     print("Game", i, "is", item)
#     i = i+1
#
#
# counter = 1
#
# while counter <= 10:
#     print(counter)
#     counter = counter + 1


# sentence = input("Enter a sentence: ")
#
# for letter in sentence:
#     if "A" == letter or "a" == letter:
#         print("X", end="")
#     else:
#         print(letter, end="")

# x = range(128)
#
# for n in x:
#     print(chr(n), end="")
# print()
# print("-" * 180)

# correctNumber = random.randint(0,100)
#
# attempt = 5
#
# while attempt > 0:
#     userGuess = int(input("Guess a number: "))
#     attempt = attempt - 1
#
#     if userGuess < 0 or userGuess > 100:
#         print("Error, guess a number from 0-100 only")
#     else:
#         if userGuess == correctNumber:
#             print("You win!")
#             break
#         else:
#             print("Wrong,", attempt, "attempts left")
#             if userGuess < correctNumber:
#                 print("Go higher")
#             elif userGuess > correctNumber:
#                 print("Go lower")
#             print("")
#
#         if attempt == 0:
#             print("You lose! The correct number is", correctNumber)


x = True

while x == True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Select an operation (Addition, Subtraction, Multiplication, Division): ")

    # Line 19-27 are the code segments for Addition and loop conditions
    if operation == "Addition":
        numValue = num1 + num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 30-38 are the code segments for Subtraction and loop conditions
    elif operation == "Subtraction":
        numValue = num1 - num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 41-49 are the code segments for Multiplication and loop conditions
    elif operation == "Multiplication":
        numValue = num1 * num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False

    # Line 52-60 are the code segments for Division and loop conditions
    elif operation == "Division":
        numValue = num1 / num2
        print("Result: %.2f" % numValue)

        userInput = input("Do you want to repeat? (Y for yes, or Q for quit): ")
        if userInput == "Y":
            x = True
        else:
            x = False