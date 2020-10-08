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
