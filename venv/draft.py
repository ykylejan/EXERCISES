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


