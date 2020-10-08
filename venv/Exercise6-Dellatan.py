# 6.1 Write a program that reads an integer and prints whether it is negative, zero, or positive.
integerInput = int(input("Enter an integer: "))
integerValue = ""

if integerInput < 0:
    integerValue = "Negative"
elif integerInput == 0:
    integerValue = "Zero"
else:
    integerValue = "Positive"

print("Result:", integerValue)
print("-" * 180)

##
# 6.2 Write a program that assigns letter grades for a quiz, according to the following table. Draw a flowchart for the algorithm.
# Score	  Grade
# 90-100	A
# 80-89	    B
# 70-79	    C
# 60-69	    D
# <60	    F
score = int(input("Enter a score: "))
gradeLetter = ""

if score > 100 or score < 0:
    print("Error. Please input scores between 0 - 100")
else:
    if score >= 90 and score <= 100:
        gradeLetter = "A"
    elif score >= 80 and score <= 89:
        gradeLetter = "B"
    elif score >= 70 and score <= 79:
        gradeLetter = "C"
    elif score >= 60 and score <= 69:
        gradeLetter = "D"
    else:
        gradeLetter = "F"

    print("Grade:", gradeLetter)
print("-" * 180)


##
# 6.3 Write a program that reads in three floating-point numbers and prints the largest of the three inputs without using the max function. For example:
#          Enter a number: 4
#          Enter a number: 9
#          Enter a number: 2.5
#          The largest number is 9.0
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

number = 0

if num1 > num2 > num3:
    number = num1
elif num1 < num2 > num3:
    number = num2
else:
    number = num3

print("The largest number is", number)
print("-" * 180)

##
# 6.4 Write a program that reads a temperature value and the letter C for Celsius or F for Fahrenheit.
# Print whether water is liquid, solid, or gaseous at the given temperature at sea level.
#
tempInput = float(input("Enter a temperature value: "))
scaleInput = input("Enter a temperature scale (C for Celsius or F for Fahrenheit): ")
temperature = ""

if scaleInput == "C" or scaleInput == "F":
    if scaleInput == "C":
        if tempInput <= -2:
            temperature = "Solid"
        elif tempInput >= 100:
            temperature = "Gaseous"
        else:
            temperature = "Liquid"
    elif scaleInput == "F":
        if tempInput <= 28.4:
            temperature = "Solid"
        elif tempInput >= 212:
            temperature = "Gaseous"
        else:
            temperature = "Liquid"
    print("Result:", temperature)
else:
    print("Error. Please input C or F for temperature scale.")

print("-" * 180)

##
# 6.5 The boiling point of water drops by about one degree Celsius for every 300 meters (or 1,000 feet) of altitude.
# Modify the program of Exercise 6.4 to allow the user to supply the altitude in meters or feet.
# Draw a flowchart for the algorithm.
#
altitudeInput = float(input("Enter altitude: "))
measureInput = input("Enter measurement scale (M for meters, or F for feet): ")

if measureInput == "M" or measureInput == "F":
    if measureInput == "M":
        boilPoint = altitudeInput / 300
    else:
        boilPoint = altitudeInput / 1000
    print("Result: The boiling point of water dropped by %.2f" % boilPoint + "°C")
else:
    print("Error. Please input M or F for the measurement scale")


