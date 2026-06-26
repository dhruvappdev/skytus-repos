#1. Read a File and Display Its Contents
file = open("data.txt", "r")

content = file.read()

print(content)

file.close()

#2. Count the Number of Lines in a File
file = open("data.txt", "r")

lines = file.readlines()

print("Total Lines =", len(lines))

file.close()

#3. Count How Many Times Each Word Appears
file = open("data.txt", "r")

text = file.read()

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

file.close()

#4. Write 5 User-Entered Sentences to a File
file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")

file.close()

print("Data saved successfully")

#5. Append a List of Strings to an Existing File
lines = [
    "Python",
    "Java",
    "C++"
]

file = open("data.txt", "a")

for line in lines:
    file.write(line + "\n")

file.close()

print("Data appended")

#6. Print Only Lines Containing a Specific Word
word = input("Enter word to search: ")

file = open("data.txt", "r")

for line in file:
    if word in line:
        print(line)

file.close()

#7. Replace a Specific Word in a File
file = open("data.txt", "r")

content = file.read()

file.close()

content = content.replace("Python", "Java")

file = open("data.txt", "w")

file.write(content)

file.close()

print("Word replaced successfully")

#8. Merge Two Text Files into a Third File
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

merged = open("merged.txt", "w")

merged.write(content1)
merged.write("\n")
merged.write(content2)

file1.close()
file2.close()
merged.close()

print("Files merged successfully")

#9. Read a CSV File and Display Its Contents
import csv

file = open("data.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()

#10. Back Up a File by Copying Its Contents
source = open("data.txt", "r")

content = source.read()

backup = open("backup.txt", "w")

backup.write(content)

source.close()
backup.close()

print("Backup created successfully")
