file = open("student.txt", "w")

file.write("Name: Rushi\n")
file.write("Roll Number: 04\n")
file.write("Branch: CSE\n")
file.write("Semester: 5\n")

file.close()

print("Data written successfully")

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()
#---------------------------------------------------

file = open("student.txt", "a")

file.write("Address: Kolhapur\n")
file.write("Mobile: 9876543210\n")

file.close()

print("Information added successfully")

file = open("student.txt", "r")

for line in file:
    print(line)

file.close()

file = open("student.txt", "r")

count = 0

for line in file:
    count = count + 1

print("Total number of lines:", count)

file.close()


file = open("student.txt", "r")

count = 0

for line in file:
    words = line.split()
    count = count + len(words)

print("Total number of words:", count)

file.close()


file = open("student.txt", "r")

count = 0

for line in file:
    count = count + len(line)

print("Total number of characters:", count)

file.close()


#---------------------------------------------------

file = open("student.txt", "r")

lines = file.readlines()

for i in range(len(lines) - 1, -1, -1):
    print(lines[i])

file.close()

file = open("student.txt", "r")

text = file.read()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

print("Vowels:", vowels)
print("Consonants:", consonants)

file.close()


file = open("student.txt", "r")

text = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

file.close()


file = open("student.txt", "r")

text = file.read()

words = text.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

file.close()



file = open("student.txt", "r")

text = file.read()

words = text.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print(frequency)

file.close()


file = open("student.txt", "r")

word = input("Enter word to search: ")

count = 0
line_no = 0

for line in file:
    line_no = line_no + 1

    words = line.split()

    for w in words:
        if w == word:
            count = count + 1
            print("Found at line:", line_no)

print("Total occurrences:", count)

file.close()



file = open("student.txt", "r")

text = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

text = text.replace(old_word, new_word)

file.close()

file = open("student.txt", "w")

file.write(text)

file.close()

print("Word replaced successfully")



file = open("program.py", "r")

lines = file.readlines()

file.close()

new_file = open("new_program.py", "w")

for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)

new_file.close()

print("Comments removed successfully")





file = open("student.txt", "r")

text = file.read()

file.close()

new_file = open("uppercase.txt", "w")

new_file.write(text.upper())

new_file.close()

print("Uppercase file created")



file = open("students.txt", "w")

file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

file = open("students.txt", "r")

students = []

print("Student Records:")

for line in file:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    marks = int(data[2])

    students.append([roll, name, marks])

    print(roll, name, marks)

file.close()

total = 0
highest = students[0]

for student in students:
    total = total + student[2]

    if student[2] > highest[2]:
        highest = student

average = total / len(students)

print("Highest marks:", highest[1])
print("Average marks:", average)

print("Students scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student[1])
        
        
        