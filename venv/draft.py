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