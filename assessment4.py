#1. Take a string input and print its length

text = input("Enter a string: ")
print("Length =", len(text))

#2. Convert a sentence to lowercase

sentence = input("Enter a sentence: ")
print(sentence.lower())

#3. Replace spaces with underscores

text = input("Enter a Text:")
print(text.replace(" ","_"))

#4. Extract the first and last character

text = input("Enter a string: ")

print("First character:", text[0])
print("Last character:", text[-1])

#5. Reverse a string using slicing

text = input("Enter a String")
print("Reversed String:",text[::-1])

#6. Count how many times a letter appears

text = input("Enter a string: ")
letter = input("Enter a letter: ")

print(text.count(letter))

#7. Check if a word is present in a sentence

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")

if word in sentence:
    print("Word found")
else:
    print("Word not found")

#8. Take name & age and print using f-string

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

#9. Remove extra spaces from start and end

text = input("Enter a string: ")

print(text.strip())

#10. Join a list with "-"

words = ["Python", "Java", "C++"]

result = "-".join(words)

print(result)


#List Programs

#11. Create a list of 5 favorite movies

movies = ["3 Idiots", "Interstellar", "Bahubali", "KGF", "Dangal"]

print(movies)

#12. Add a new movie

movies = ["3 Idiots", "Interstellar", "Bahubali"]

movies.append("KGF")

print(movies)

#13. Remove the first movie

movies = ["3 Idiots", "Interstellar", "Bahubali"]

movies.pop(0)

print(movies)

#14. Sort numbers in ascending order

numbers = [45, 12, 8, 99, 23]

numbers.sort()

print(numbers)

#15. Reverse a list

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)

#16. Find the largest number

numbers = [10, 45, 23, 89, 12]

print(max(numbers))

#17. Merge two lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2

print(merged)

#18. Access the last element

numbers = [10, 20, 30, 40, 50]

print(numbers[-1])

#19. Nested list and access inner element

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(data[1][2])

#20. Count how many times an element appears

numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))
