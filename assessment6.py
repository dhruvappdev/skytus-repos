#1. Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

#2. Display multiplication table for a given number
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#3. Find factorial of a number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial =", factorial)

#4. Generate first N Fibonacci numbers
n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c

#5. Check if a number is prime
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

#6. Reverse a number (e.g., 123 → 321)
num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)

#7. Count digits in a number
num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += 1
    num = num // 10

print("Total Digits =", count)

#8. Find sum of even numbers between 1 and 100
total = 0

for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Sum =", total)

#9. Print a pyramid pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print("*" * i)

#10. Find all divisors of a number
num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

