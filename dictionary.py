# 1. Student details dictionary
student = {
    "roll_no": 101,
    "name": "Rahul",
    "department": "CSE",
    "marks": 85
}

for key in student:
    print(key, ":", student[key])


# 2. Employee information and specified key
employee = {
    "id": 101,
    "name": "Amit",
    "department": "HR",
    "salary": 40000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")


# 3. Add a new product and price
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 100,
    "Pencil": 5
}

products["Notebook"] = 40

print(products)


# 4. Update marks of a specified student
marks = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")


# 5. Remove a specified city
cities = {
    "Pune": 7000000,
    "Mumbai": 12000000,
    "Kolhapur": 500000,
    "Nashik": 2000000
}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")


# 6. Check whether employee ID exists
employees = {
    101: "Rahul",
    102: "Amit",
    103: "Sneha"
}

employee_id = int(input("Enter employee ID: "))

if employee_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


# 7. Count total key-value pairs
students = {
    "Rahul": 85,
    "Amit": 78,
    "Sneha": 92,
    "Priya": 88
}

print("Total key-value pairs:", len(students))


# 8. Display keys, values and key-value pairs
data = {
    "Name": "Rahul",
    "Age": 20,
    "Marks": 85
}

print("Keys:")
print(data.keys())

print("Values:")
print(data.values())

print("Key-value pairs:")
print(data.items())


# 9. Programming languages and creators
languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}

for language in languages:
    print(language, ":", languages[language])


# 10. Accept five student names and marks
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)


# 11. Student with highest marks
marks = {
    "Rahul": 85,
    "Amit": 78,
    "Sneha": 92,
    "Priya": 88
}

highest_name = ""
highest_marks = -1

for name in marks:
    if marks[name] > highest_marks:
        highest_marks = marks[name]
        highest_name = name

print("Highest marks:", highest_name, highest_marks)


# 12. Student with lowest marks
marks = {
    "Rahul": 85,
    "Amit": 78,
    "Sneha": 92,
    "Priya": 88
}

lowest_name = ""
lowest_marks = 101

for name in marks:
    if marks[name] < lowest_marks:
        lowest_marks = marks[name]
        lowest_name = name

print("Lowest marks:", lowest_name, lowest_marks)


# 13. Average marks of all students
marks = {
    "Rahul": 85,
    "Amit": 78,
    "Sneha": 92,
    "Priya": 88
}

total = 0

for name in marks:
    total = total + marks[name]

average = total / len(marks)

print("Average marks:", average)


# 14. Character frequency in a string
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

print(frequency)


# 15. Word frequency in a sentence
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print(frequency)


# 16. Merge two dictionaries
dict1 = {
    "a": 10,
    "b": 20
}

dict2 = {
    "c": 30,
    "d": 40
}

merged = dict1.copy()
merged.update(dict2)

print(merged)


# 17. Common keys in two dictionaries
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}

common = []

for key in dict1:
    if key in dict2:
        common.append(key)

print("Common keys:", common)


# 18. Common values in two dictionaries
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 30,
    "y": 40,
    "z": 20
}

common = []

for key in dict1:
    if dict1[key] in dict2.values():
        if dict1[key] not in common:
            common.append(dict1[key])

print("Common values:", common)


# 19. Remove duplicate values while retaining keys
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new_data = {}

for key in data:
    if data[key] not in new_data.values():
        new_data[key] = data[key]

print(new_data)


# 20. Display dictionary in ascending order of keys
data = {
    4: "D",
    1: "A",
    3: "C",
    2: "B"
}

keys = list(data.keys())
keys.sort()

for key in keys:
    print(key, ":", data[key])


# 21. Numbers 1 to 10 and their squares
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print(squares)


# 22. Even numbers from 1 to 20 and their squares
squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i

print(squares)


# 23. Frequency of unique numbers in a list
numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1

print(frequency)


# 24. Numbers 1 to 10 and their cubes
cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print(cubes)


# 25. Student dictionary operations
students = {
    "Rahul": 80,
    "Amit": 75,
    "Sneha": 90
}

students["Priya"] = 85

students["Amit"] = 82

del students["Rahul"]

name = input("Enter student to search: ")

if name in students:
    print("Student found:", students[name])
else:
    print("Student not found")

print("All students:")
for name in students:
    print(name, students[name])

highest = -1
total = 0

for name in students:
    if students[name] > highest:
        highest = students[name]
    total = total + students[name]

average = total / len(students)

print("Highest marks:", highest)
print("Average marks:", average)


# 26. Employee salary operations
salaries = {
    "Rahul": 45000,
    "Amit": 55000,
    "Sneha": 65000,
    "Priya": 30000
}

highest = 0
lowest = salaries["Rahul"]
total = 0

for name in salaries:
    if salaries[name] > highest:
        highest = salaries[name]
    if salaries[name] < lowest:
        lowest = salaries[name]
    total = total + salaries[name]

average = total / len(salaries)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than 50000:")
for name in salaries:
    if salaries[name] > 50000:
        print(name)


# 27. Product quantity operations
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15,
    "Bottle": 8
}

products["Pencil"] = 25

products["Book"] = 12

del products["Pen"]

name = input("Enter product to search: ")

if name in products:
    print("Product found. Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name in products:
    if products[name] < 10:
        print(name, products[name])


# 28. Contact dictionary operations
contacts = {
    "Rahul": "9876543210",
    "Amit": "9876501234"
}

contacts["Sneha"] = "9876512345"

name = input("Enter contact to search: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found")

name = input("Enter contact to update: ")

if name in contacts:
    number = input("Enter new phone number: ")
    contacts[name] = number
else:
    print("Contact not found")

name = input("Enter contact to delete: ")

if name in contacts:
    del contacts[name]
else:
    print("Contact not found")

print("All contacts:")
for name in contacts:
    print(name, contacts[name])


# 29. Book ID and book name operations
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

books[104] = "HTML"

book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]
else:
    print("Book not found")

print("All books:")
for book_id in books:
    print(book_id, books[book_id])

print("Total books:", len(books))


# 30. Group students according to department
students = {
    "Rahul": "CSE",
    "Amit": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Rohit": "IT"
}

departments = {}

for name in students:
    department = students[name]

    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print(departments)


# 31. Group words according to word length
words = ["cat", "dog", "apple", "book", "pen", "banana"]

result = {}

for word in words:
    length = len(word)

    if length not in result:
        result[length] = []

    result[length].append(word)

print(result)


# 32. Find two numbers whose sum is equal to target
numbers = [2, 7, 11, 15, 3, 6]
target = 9

number_dict = {}

for number in numbers:
    required = target - number

    if required in number_dict:
        print("Numbers are:", required, number)
        break

    number_dict[number] = number


# 33. First character that occurs only once
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

found = False

for ch in text:
    if frequency[ch] == 1:
        print("First unique character:", ch)
        found = True
        break

if found == False:
    print("No unique character found")


# 34. First character that occurs more than once
text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

found = False

for ch in text:
    if frequency[ch] > 1:
        print("First repeated character:", ch)
        found = True
        break

if found == False:
    print("No repeated character found")


# 35. Word length and number of words having that length
paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)

    if length in result:
        result[length] = result[length] + 1
    else:
        result[length] = 1

print(result)
