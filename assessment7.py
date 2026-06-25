#1. Create a Custom Math Module and Import It

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

import mymath

print(mymath.add(10, 5))
print(mymath.subtract(10, 5))

#2. Create a Module for String Operations
def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

import string_utils

print(string_utils.to_upper("python"))
print(string_utils.to_lower("PYTHON"))

#3. Generate 5 Random Integers
import random

for i in range(5):
    print(random.randint(1, 100))

#4. Display Current Date and Time
from datetime import datetime

now = datetime.now()

print("Current Date and Time:")
print(now)

#5. Find Factorial Using Math Module
import math

num = int(input("Enter a number: "))

print("Factorial =", math.factorial(num))

#6. Create a Package for Circle and Rectangle
"""shapes/
│
├── __init__.py
├── circle.py
└── rectangle.py""""

def area(radius):
    return 3.14 * radius * radius

def area(length, width):
    return length * width

from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

print(circle_area(5))
print(rectangle_area(10, 4))

#7. Import Multiple Functions from One Module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

from calculator import add, multiply

print(add(5, 3))
print(multiply(5, 3))

#8. Shuffle a List Using Random Module
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

#9. Calculate Difference Between Two Dates
from datetime import date

date1 = date(2026, 6, 1)
date2 = date(2026, 6, 10)

difference = date2 - date1

print("Difference =", difference.days, "days")

#10. List Files in a Directory Using os Module
import os

files = os.listdir()

print(files)

import os

files = os.listdir("C:/Users")

print(files)