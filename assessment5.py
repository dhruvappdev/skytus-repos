#1. Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)

print(numbers)

#2. Access the third element in a tuple
numbers = (10, 20, 30, 40, 50)

print(numbers[2])

#3. Unpack a tuple into separate variables
student = ("Shivam", 20, "Surat")

name, age, city = student

print(name)
print(age)
print(city)

#Set Programs

#4. Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

print(fruits)

#5. Add a new fruit to the set
fruits = {"Apple", "Banana", "Mango"}

fruits.add("Orange")

print(fruits)

#6. Remove an element from a set
fruits = {"Apple", "Banana", "Mango"}

fruits.remove("Banana")

print(fruits)

#7. Find union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

#8. Find intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))

#9. Check if one set is a subset of another
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))

#10. Remove duplicates using a set
numbers = [1, 2, 3, 2, 4, 1, 5]

unique_numbers = set(numbers)

print(unique_numbers)

#Dictionary Programs

#11. Create a dictionary storing student names and marks
marks = {
    "Shivam": 90,
    "Rahul": 85,
    "Aman": 95
}

print(marks)

#12. Add a new key-value pair
marks = {
    "Shivam": 90,
    "Rahul": 85
}

marks["Aman"] = 95

print(marks)

#13. Delete a key-value pair
marks = {
    "Shivam": 90,
    "Rahul": 85,
    "Aman": 95
}

del marks["Rahul"]

print(marks)

#14. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)

print(dict1)

#15. Check if a key exists
student = {
    "name": "Shivam",
    "age": 20
}

print("name" in student)

#16. Count word frequency using a dictionary
text = "apple banana apple mango banana apple"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

#17. Find the key with the maximum value
marks = {
    "Shivam": 90,
    "Rahul": 85,
    "Aman": 95
}

highest = max(marks, key=marks.get)

print(highest)

#18. Reverse keys and values
student = {
    "name": "Shivam",
    "city": "Surat"
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print(reversed_dict)

#19. Update the value for a specific key
student = {
    "name": "Shivam",
    "age": 20
}

student["age"] = 21

print(student)

#20. Convert a list of tuples into a dictionary
data = [
    ("name", "Shivam"),
    ("age", 20),
    ("city", "Surat")
]

result = dict(data)

print(result)