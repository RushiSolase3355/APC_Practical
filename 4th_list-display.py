#1----------------------------------------------------

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print(fruits)

print("\n")
#2------------------------------------------------------------

list =[1,2,3,4,5]

print("first element is:", list[0])
print("second element is :", list[1])
print("last element is :", list[4])

print("\n")

#3-------------------------------------------------------------

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

print("Original list:")
print(colors)

# Replace third color
colors[2] = "White"

print("Updated list:")
print(colors)

print("\n")

#4-------------------------------------------------------------

list = [20,30,40,50,90]

print("org list:",list)

list.append(100)

list.insert(0,90)

list.insert(3,77)

print("updates list is :", list)
print("\n")

#5--------------------------------------------------------------

students =["thor","ironman","spiderman","hulk"]

print("orig list:",students)

students.pop(0)
students.pop()
students.remove("spiderman")

print("updated list is :",students)

print("\n")

#6- largest and smallest number in a list------------------------

numbers = [10,20,30,40,76,2,90,56]

largest = numbers[0]
smallest = numbers[0]


for i in numbers:
    if i > largest:
        largest = i
        
    elif i < smallest:
        smallest = i

print("largest number is:",largest)
print("smallest number is :",smallest)
print("\n")

#7 accept 10 nunber from user and store it in the a list---------------------

numbers = []

for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

sum = 0

for i in numbers:
    sum = sum + i

average = sum / 10

print("Sum =", sum)
print("Average =", average)
print("\n")

#8 count even and odd-------------------------

numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 11, 22, 33, 44, 55, 66]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)

#10 Reverse a list without using reverse() ------------------------------
numbers = [10, 20, 30, 40, 50]

reverse = []

for i in numbers:
    reverse.insert(0, i)

print("Original list:")
print(numbers)

print("Reverse list:")
print(reverse)


# --------------------------------------------------
# 11. First 5, Last 5, Middle 4, Alternate, Reverse

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("\n11. List Slicing")
print("First 5:", numbers[:5])
print("Last 5:", numbers[5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])


# --------------------------------------------------
# 12. Display elements at even index positions

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("\n12. Even Index Elements")
for i in range(0, len(numbers), 2):
    print(numbers[i])


# --------------------------------------------------
# 13. Sort 10 numbers in ascending and descending order

numbers = []

print("\n13. Sorting")
for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)

numbers.sort()
print("Ascending:", numbers)

numbers.sort(reverse=True)
print("Descending:", numbers)


# --------------------------------------------------
# 14. Display only unique elements

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("\n14. Unique Elements")
print(unique)


# --------------------------------------------------
# 15. Find the second largest element

numbers = [10, 40, 20, 50, 30]

numbers.sort()

print("\n15. Second Largest")
print("Second largest:", numbers[-2])


# --------------------------------------------------
# 16. Nested list of student name, roll number and marks

students = [
    ["Rahul", 1, 85],
    ["Amit", 2, 78],
    ["Sneha", 3, 92]
]

print("\n16. Student Details")
for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# --------------------------------------------------
# 17. Addition of two 3 x 3 matrices

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\n17. Matrix Addition")
for row in result:
    print(row)


# --------------------------------------------------
# 18. Shopping cart operations

cart = ["Pen", "Book", "Bag"]

print("\n18. Shopping Cart")
print("Original cart:", cart)

cart.append("Bottle")
print("After adding:", cart)

cart.remove("Pen")
print("After removing:", cart)

item = "Book"
if item in cart:
    print(item, "is present")
else:
    print(item, "is not present")

print("Cart:", cart)
print("Total items:", len(cart))


# --------------------------------------------------
# 19. Student attendance list

students = ["Rahul", "Amit", "Sneha", "Priya"]

print("\n19. Student Attendance")
print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print(name, "is present")
else:
    print(name, "is absent")

students.append("Rohit")
print("After adding new student:", students)

students.remove("Amit")
print("After removing absent student:", students)


# --------------------------------------------------
# 20. Book list operations

books = ["Python", "Java", "C++"]

print("\n20. Book List")

books.append("HTML")
print("After adding book:", books)

book = input("Enter book to search: ")

if book in books:
    print("Book is available")
else:
    print("Book is not available")

books.remove("Java")
print("After removing book:", books)

print("All books:", books)
print("Total books:", len(books))


# --------------------------------------------------
# 21. Merge two lists

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

merged = list1 + list2

print("\n21. Merged List")
print(merged)


# --------------------------------------------------
# 22. Find common elements between two lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("\n22. Common Elements")
print(common)


# --------------------------------------------------
# 23. Count frequency of each element

numbers = [10, 20, 10, 30, 20, 10, 40]

print("\n23. Frequency")

checked = []

for i in numbers:
    if i not in checked:
        count = 0
        for j in numbers:
            if i == j:
                count = count + 1
        print(i, ":", count)
        checked.append(i)


# --------------------------------------------------
# 24. Rotate list left and right by one position

numbers = [10, 20, 30, 40, 50]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("\n24. List Rotation")
print("Original:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)


# --------------------------------------------------
# 25. Remove duplicates while preserving original order

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

new_list = []

for i in numbers:
    if i not in new_list:
        new_list.append(i)

print("\n25. Remove Duplicates")
print(new_list)


# --------------------------------------------------
# 26. Marks of 20 students

marks = [75, 82, 65, 90, 55, 72, 88, 60, 95, 70,
         68, 80, 77, 92, 58, 85, 73, 66, 89, 76]

highest = marks[0]
lowest = marks[0]
total = 0

for i in marks:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total = total + i

average = total / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above = above + 1
    elif i < average:
        below = below + 1

print("\n26. Student Marks")
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)


# --------------------------------------------------
# 27. Employee salaries

salaries = [25000, 35000, 55000, 45000, 60000, 28000, 70000, 32000]

highest = salaries[0]
lowest = salaries[0]
total = 0

for i in salaries:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total = total + i

average = total / len(salaries)

print("\n27. Employee Salaries")
print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning above 50000:")
for i in salaries:
    if i > 50000:
        print(i)

print("Employees earning below 30000:")
for i in salaries:
    if i < 30000:
        print(i)


# --------------------------------------------------
# 28. Batsman scores in 10 matches

scores = [45, 100, 75, 120, 35, 60, 110, 50, 25, 80]

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for i in scores:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

    total = total + i

    if i >= 100:
        centuries = centuries + 1
    elif i >= 50:
        half_centuries = half_centuries + 1

average = total / len(scores)

print("\n28. Batsman Scores")
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)


# --------------------------------------------------
# 29. Temperature of 30 days

temperature = [
    28, 30, 27, 32, 35, 31, 29, 33, 34, 30,
    26, 28, 36, 37, 32, 31, 29, 35, 33, 30,
    27, 28, 34, 36, 32, 31, 29, 33, 35, 30
]

hottest = temperature[0]
coldest = temperature[0]
total = 0

for i in temperature:
    if i > hottest:
        hottest = i
    if i < coldest:
        coldest = i
    total = total + i

average = total / len(temperature)

above = 0
below = 0

for i in temperature:
    if i > average:
        above = above + 1
    elif i < average:
        below = below + 1

print("\n29. Temperature")
print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)


# --------------------------------------------------
# 30. Patient names and ages

patients = [
    ["Rahul", 20],
    ["Amit", 25],
    ["Sneha", 22]
]

print("\n30. Patient List")

# Add patient
patients.append(["Priya", 30])

print("After adding patient:")
print(patients)

# Delete patient
patients.remove(["Amit", 25])

print("After deleting patient:")
print(patients)

# Search patient
name = input("Enter patient name to search: ")

found = False

for patient in patients:
    if patient[0] == name:
        print("Patient found")
        print("Name:", patient[0])
        print("Age:", patient[1])
        found = True

if found == False:
    print("Patient not found")

# Display all patients
print("All patients:")
for patient in patients:
    print("Name:", patient[0], "Age:", patient[1])

# Count patients
print("Total patients:", len(patients))





