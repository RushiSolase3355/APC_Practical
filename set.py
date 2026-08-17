# 1. Create and display a set of five integers
numbers = {10, 20, 30, 40, 50}

for i in numbers:
    print(i)


# 2. Convert a list with duplicate values into a set
numbers = [10, 20, 10, 30, 20, 40, 30]

numbers = set(numbers)

print(numbers)


# 3. Add two fruits to a set
fruits = {"Apple", "Mango", "Banana", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print(fruits)


# 4. Remove a specified number from a set
numbers = {10, 20, 30, 40, 50}

n = int(input("Enter number to remove: "))

if n in numbers:
    numbers.remove(n)
    print(numbers)
else:
    print("Number not found")


# 5. Check whether a student exists in a set
students = {"Rahul", "Amit", "Sneha", "Priya"}

name = input("Enter student name: ")

if name in students:
    print("Student is present")
else:
    print("Student is not present")


# 6. Find total number of cities
cities = {"Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur"}

print("Total cities:", len(cities))


# 7. Display programming languages using a loop
languages = {"Python", "Java", "C", "C++"}

for language in languages:
    print(language)


# 8. Remove duplicate numbers using a set
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers = set(numbers)

print(numbers)


# 9. Find union of two sets
set1 = {10, 20, 30}
set2 = {30, 40, 50}

result = set1.union(set2)

print("Union:", result)


# 10. Find common elements of two sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.intersection(set2)

print("Common elements:", result)


# 11. Find elements present in only one set
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Only in first set:", set1 - set2)
print("Only in second set:", set2 - set1)


# 12. Find elements present in either set but not both
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)


# 13. Check whether first set is a subset of second set
set1 = {10, 20}
set2 = {10, 20, 30, 40}

if set1.issubset(set2):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")


# 14. Check whether first set is a superset of second set
set1 = {10, 20, 30, 40}
set2 = {10, 20}

if set1.issuperset(set2):
    print("First set is a superset of second set")
else:
    print("First set is not a superset of second set")


# 15. Check whether two sets have no common elements
set1 = {10, 20, 30}
set2 = {40, 50, 60}

if set1.isdisjoint(set2):
    print("Sets have no common elements")
else:
    print("Sets have common elements")


# 16. Check whether two sets are equal
set1 = {10, 20, 30}
set2 = {30, 20, 10}

if set1 == set2:
    print("Both sets are equal")
else:
    print("Sets are not equal")


# 17. Find subjects studied by both students
student1 = {"Python", "Java", "Maths", "DBMS"}
student2 = {"Python", "C++", "Maths", "Networking"}

common = student1.intersection(student2)

print("Subjects studied by both:", common)


# 18. Display unique words from a sentence
sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)


# 19. Compare morning and afternoon attendance
morning = {"Rahul", "Amit", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Rohit", "Neha"}

print("Present in both:", morning.intersection(afternoon))
print("Only in morning:", morning - afternoon)
print("Only in afternoon:", afternoon - morning)
print("Present in at least one session:", morning.union(afternoon))


# 20. Students enrolled in Python and Java
python_students = {"Rahul", "Amit", "Sneha", "Rohit"}
java_students = {"Amit", "Sneha", "Priya", "Neha"}

print("Python students:", python_students)
print("Java students:", java_students)


# 21. Find students in both courses and only one course
python_students = {"Rahul", "Amit", "Sneha", "Rohit"}
java_students = {"Amit", "Sneha", "Priya", "Neha"}

both = python_students.intersection(java_students)
only_one = python_students.symmetric_difference(java_students)

print("Students in both:", both)
print("Students in only one course:", only_one)


# 22. Compare technical skills of two employees
employee1 = {"Python", "Java", "SQL", "HTML"}
employee2 = {"Python", "C++", "SQL", "CSS"}

print("Common skills:", employee1.intersection(employee2))
print("Skills only in Employee 1:", employee1 - employee2)
print("Skills only in Employee 2:", employee2 - employee1)
print("All skills:", employee1.union(employee2))


# 23. Find requested books that are available
available_books = {"Python", "Java", "C++", "DBMS"}
requested_books = {"Python", "DBMS", "HTML", "Networking"}

available = requested_books.intersection(available_books)

print("Requested books available:", available)


# 24. Compare visitors from two days
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("Only first day:", day1 - day2)
print("Only second day:", day2 - day1)


# 25. Find products common to two categories
category1 = {"Pen", "Book", "Bag", "Bottle"}
category2 = {"Book", "Bottle", "Pencil", "Notebook"}

common = category1.intersection(category2)

print("Products in both categories:", common)


# 26. Find mutual and unique friends of two users
user1 = {"Rahul", "Amit", "Sneha", "Rohit"}
user2 = {"Sneha", "Rohit", "Priya", "Neha"}

print("Mutual friends:", user1.intersection(user2))
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1.union(user2)))
