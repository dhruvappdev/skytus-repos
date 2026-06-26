#1. Function to Check if a Number is Prime
def is_prime(num):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

#2. Function to Reverse a String
def reverse_string(text):
    return text[::-1]


text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))

#33. Function to Find Factorial
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result


num = int(input("Enter a number: "))

print("Factorial =", factorial(num))

#4. Function to Calculate Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100


principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

print("Simple Interest =", simple_interest(principal, rate, time))

#5. Function to Check if a Word is Palindrome
def is_palindrome(word):
    return word == word[::-1]


word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")

#6. Function to Count Vowels in a String
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count


text = input("Enter a string: ")

print("Number of vowels =", count_vowels(text))

#7. Function to Merge Two Lists
def merge_lists(list1, list2):
    return list1 + list2


list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(merge_lists(list1, list2))

#8. Function to Find GCD of Two Numbers
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", find_gcd(num1, num2))

#9. Function to Find Area of Rectangle
def area_rectangle(length, width):
    return length * width


length = float(input("Enter length: "))
width = float(input("Enter width: "))

print("Area =", area_rectangle(length, width))

#10. Function to Check Armstrong Number
def is_armstrong(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10

    return total == num


num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

