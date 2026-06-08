# 1. Remainder of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Remainder =", a % b)

# 2. Even or Odd

num = int(input("Enter a number: "))

print("Even" if num % 2 == 0 else "Odd")

# 3. Larger number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Larger number =", max(a, b))

# 4. Square and Cube

num = int(input("Enter a number: "))

print("Square =", num**2)
print("Cube =", num**3)

# 5. Check equal numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a == b)

# 6. Both numbers positive

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > 0 and b > 0)

# 7. Float to Integer

num = float(input("Enter a float number: "))

print(int(num))

# 8. String to int and multiply by 10

num = input("Enter a number: ")

print(int(num) * 10)

# 9. Using and / or operators

age = int(input("Enter age: "))
license = input("Do you have license (True/False): ") == "True"

print(age >= 18 and license)
print(age < 18 or not license)

# 10. Quotient and Remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient =", a // b)
print("Remainder =", a % b)