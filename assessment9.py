#1. Check if a Person is Eligible to Vote
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#2. Grade Calculator
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")

#3. Traffic Light Simulator
signal = input("Enter signal color (Red/Yellow/Green): ")

if signal == "Red":
    print("Stop")
elif signal == "Yellow":
    print("Wait")
elif signal == "Green":
    print("Go")
else:
    print("Invalid Signal")

#4. ATM Withdrawal Check
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if balance >= amount:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

#5. Check Positive, Negative, or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

#6. Check if Number Lies Within a Range
num = int(input("Enter a number: "))

if num >= 1 and num <= 100:
    print("Number is within the range")
else:
    print("Number is outside the range")

#7. Username & Password Verification
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")

#8. Electricity Bill Calculator
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Electricity Bill =", bill)

#9. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print("Result =", num1 + num2)

elif operation == "-":
    print("Result =", num1 - num2)

elif operation == "*":
    print("Result =", num1 * num2)

elif operation == "/":
    print("Result =", num1 / num2)

else:
    print("Invalid Operation")

#10. Check Type of Triangle
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles Triangle")

else:
    print("Scalene Triangle")

