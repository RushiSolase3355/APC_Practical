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


