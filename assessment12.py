#1. Handle Division by Zero Error
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

#2. Handle Invalid Integer Input
try:
    num = int(input("Enter a number: "))

    print("You entered:", num)

except ValueError:
    print("Invalid input. Please enter an integer.")

#3. Handle "File Not Found" Error
try:
    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found")

#4. Multiple Exception Blocks
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(num1 / num2)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

#5. Use finally for Cleanup
try:
    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program finished")

#6. Custom Exception for Invalid Age
age = int(input("Enter age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above")

    print("Valid age")

except Exception as e:
    print(e)

#7. Handle IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range")

#8. Catch All Possible Errors
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(num1 / num2)

except Exception as e:
    print("Error:", e)

#9. Log Errors to a File
try:
    num = int(input("Enter a number: "))

except Exception as e:
    file = open("error_log.txt", "a")

    file.write(str(e) + "\n")

    file.close()

    print("Error saved to file")

#10. Validate Email Format
email = input("Enter email: ")

try:
    if "@" not in email or "." not in email:
        raise Exception("Invalid Email Format")

    print("Valid Email")

except Exception as e:
    print(e)

