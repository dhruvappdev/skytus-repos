#1. Print Name, Age, and City in One Line

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(name, age, city)

#2. Add Two Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum is:", sum)

#3. Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit is:", fahrenheit)

#4. Print Name in Uppercase

name = input("Enter your name: ")

print(name.upper())

#5. Calculate Current Age from Birth Year

birth_year = int(input("Enter your birth year: "))

current_age = 2026 - birth_year

print("Your age is:", current_age)

#6. Swap Two Variables

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

#7. Area of Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of rectangle is:", area)

#8. Check Positive or Negative Number

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Number is zero")

#9. Find Average of Two Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2

print("Average is:", average)


