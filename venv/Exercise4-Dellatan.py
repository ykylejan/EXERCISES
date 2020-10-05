## 4.1 Write a program that prompts the user for two integers and then prints (The sum, The difference, The product, The average, The distance, The maximum and minimum)
integerInput1 = input("Enter the first number: ")
num1 = int(integerInput1)
integerInput2 = input("Enter the second number: ")
num2 = int(integerInput2)

integerSum = num1 + num2
integerDifference = num1 - num2
integerProduct = num1 * num2
integerAverage = (num1 + num2) / 2
integerDistance = abs(integerDifference)
integerMaximum = max(num1, num2)
integerMinimum = min(num1, num2)

print(" ")
print("Sum:", integerSum)
print("Difference:", integerDifference)
print("Product:", integerProduct)
print("Average: %.2f" % integerAverage)
print("Distance:", integerDistance)
print("Maximum:", integerMaximum)
print("Minimum:", integerMinimum)
print(" ")

## 4.2 Write a program that prompts the user for a radius and then prints the following.
# The area and circumference of a circle with that radius
radiusInput = input("Enter a Radius: ")
radius = float(radiusInput)
mathPi = 3.14159265359

circleArea = (radius ** 2) * mathPi
circleCircumference = mathPi * (radius) * 2

print(" ")
print("Circle Area: %.2f" % circleArea)
print("Circle Circumference: %.2f" % circleCircumference)
print(" ")

# The volume and surface area of a sphere with that radius
sphereVolume = (4 / 3) * (mathPi * (radius ** 3))
sphereSurfaceArea = 4 * (mathPi * (radius ** 2))

print("Sphere Volume: %.2f" % sphereVolume)
print("Sphere Surface Area: %.2f" % sphereSurfaceArea)
print(" ")

## 4.3 File names and extensions. Write a program that prompts the user for the drive letter, the path, the file name, and the extension.
# Then print the complete file name. Example:
# • Drive letter: C
# • Path: \Windows\System
# • File name: Readme
# • Extension: txt

inputDriveLetter = input("Enter Drive letter: ")
inputPath = input("Enter Path: ")
inputFileName = input("Enter File name: ")
inputExtension = input("Enter Extenstion: ")

print(" ")
print(inputDriveLetter + ":" + inputPath + "\\" + inputFileName + "." + inputExtension)

# 4.4 Printing a grid. Write a program that prints the following grid to play tic-tac-toe. (Print the comb three times and the bottom line once.)
combLine = '''+---+---+---+
|   |   |   |'''
bottomLine = "+---+---+---+"

print(" ")
print(combLine)
print(combLine)
print(combLine)
print(bottomLine)
print(" ")

# 4.5 The following algorithm describes how a bookstore computes the price of an order from the total price and the number of the books that were ordered.
# • Read the total book price and the number of books.
# • Compute the tax (7.5 percent of the total book price).
# • Compute the shipping charge (25 per book).
# • The price of the order is the sum of the total book price, the tax, and the shipping charge.
# • Print the price of the order.

priceInput = input("Enter Price: ")
price = float(priceInput)
quantityInput = input("Enter Quantity: ")
quantity = float(quantityInput)

tax = price * 0.075
shippingFee = quantity * 25

priceOrder = (price + tax) + shippingFee

print(" ")
print("Price Order: %.2f" % priceOrder)