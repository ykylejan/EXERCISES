##
# 7.1 Write a program that reads in three
# strings and sorts them lexicographically. Example:
# Enter a string: Charlie
# Enter a string: Able
# Enter a string: Baker
#
# Able Baker Charlie
#

name1 = input("Enter a String: ")
name2 = input("Enter a String: ")
name3 = input("Enter a String: ")

if name1.isalpha():
    if name1 < name2 and name1 < name3:
        print(name1, min(name2, name3), max(name2, name3))
    elif name2 < name1 and name2 < name3:
        print(name2, min(name1, name3), max(name1, name3))
    else:
        print(name3, min(name1, name2), max(name1, name2))
else:
    print("Error, input string only")



print("-" * 180)


##
# 7.2 Write a program that reads in a string and prints whether it
# contains only letters
# contains only uppercase letters
# contains only lowercase letters
# contains only digits
# contains only letters and digits
# starts with an uppercase letter
# ends with a period.
#

stringName = input("Enter a string: ")

if stringName.isalpha():
    print("It contains letters")
    if stringName.isupper():
        print("It contains uppercase letters")
    if stringName.islower():
        print("It contains lowercase letters")
if stringName.isdigit():
    print("It contains digits ")
if stringName.isalnum():
    print("It contatin letters and digits")
if stringName[0].isupper():
    print("It starts with an uppercase letter")
if stringName.endswith("."):
    print("It ends with a period")

print("-" * 180)

##
# 7.3 Write a program that prompts the user to provide a single character from the alphabet.
# Print Vowel or Consonant, depending on the user input.
# If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.
#
character = input("Enter a single alphabet character: ")
vowel = "aeiouAEIOU"

if len(character) > 1:
    print("Error, single alphabet character only")
else:
    if vowel.find(character) != -1:
        print("Vowel")
    elif character.isalpha():
        print("Consonant")

print("-" * 180)

##
# 7.4 Read in a time such as 3 pm and print the equivalent military hour (such as 15). Validate the input.
# If the number isn’t between 1 and 12, print: Error: The hourmust be between 1 and 12.
# If the suffix isn’t "am" or "pm", print: Error: The suffix must be am or pm.
#
time = int(input("Enter a time: "))
suffix = input("Enter am or pm: ")

if suffix == "am" or suffix == "pm":
    if time >= 13:
        print("Error, 1-12 only")
    else:
        if suffix == "pm":
            if time == 1: print("13")
            elif time == 2: print("14")
            elif time == 3: print("15")
            elif time == 4: print("16")
            elif time == 5: print("17")
            elif time == 6: print("18")
            elif time == 7: print("19")
            elif time == 8: print("20")
            elif time == 9: print("21")
            elif time == 10: print("22")
            elif time == 11: print("23")
            elif time == 12: print("0")
        else:
            print(time)
else:
    print("Error, am or pm only")

print("-" * 180)

##
# 7.5 Write a program that reads the French name of a country and adds the article:
# le for masculine or la for feminine, such as le Canada or la Belgique.
# However, if the country name starts with a vowel, use l’; for example, l’Afghanistan.
#
country = input("Enter country: ")

if country.isalpha():
    if country.startswith(vowel):
        print("l", country)
    else:
        if country.endswith("e"):
            if country == "Belize":
                print("le", country)
            elif country == "Cambodge":
                print("le", country)
            elif country == "Mexique":
                print("le", country)
            elif country == "Mozambique":
                print("le", country)
            elif country == "Zaïre":
                print("le", country)
            elif country == "Zimbabwe":
                print("le", country)
            else:
                print("la", country)
        elif country.endswith("s"):
            print("les", country)
        else:
            print("le", country)
else:
    print("Error, country names only.")




