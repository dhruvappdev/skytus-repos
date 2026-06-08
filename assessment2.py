# 1. Calculate the remainder of two numbers

num1 = 17
num2 = 5

remainder = num1 % num2

print("Remainder is:", remainder)

# 2. Check if a number is even or odd

num = 8

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 3. Compare two numbers and print the larger one

a = 25
b = 40

if a > b:
    print(a, "is larger")
else:
    print(b, "is larger")

# 4. Calculate square and cube of a number

num = 4

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)

# 5. Check if two entered numbers are equal

num1 = 10
num2 = 10

if num1 == num2:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")

# 6. Check if both numbers are positive

a = 5
b = 9

result = a > 0 and b > 0

print(result)

# 7. Convert float to integer

num = 12.75

integer_num = int(num)

print("Integer value:", integer_num)

# 8. Take a number as string, convert to int, and multiply by 10

num = "7"

result = int(num) * 10

print(result)

# 9. Use and & or operators to check multiple conditions

age = 20
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or not has_license:
    print("Cannot drive")

# 10. Divide two numbers and print quotient and remainder separately

num1 = 20
num2 = 3

quotient = num1 // num2
remainder = num1 % num2

print("Quotient =", quotient)
print("Remainder =", remainder)