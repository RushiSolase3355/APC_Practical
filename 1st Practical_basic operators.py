# Basic Data Types

x = 100
print(type(x))

x = "hello"
print(type(x))

x = 3.14
print(type(x))

# i is not defined, so this will give an error
# x = i + 1

x = ["apple", "banana", "fruit"]
print(type(x))

# range() needs an integer
# range(x) will not work because x is a list

x = {"apple", "banana"}
print(type(x))

x = ("apple", "banana")
print(type(x))

# range() needs an integer
# range(x) will not work because x is a tuple

x = ("apple", "banana")
print(type(x))

x = {("banana", "apple")}
print(type(x))

x = frozenset(["apple", "banana"])
print(type(x))


# List

x = ["10", "20", "30"]

x.append(40)

print(x)

# Correct way to access list element
print(x[2])


# Tuple

y = (21, 45, 88)

x = ("apple", "banana")

# Tuple does not support append()
# x.append(90)


# Operators


# Arithmetic Operators

x = 1 + 6
print(x)

x = 68 - 45
print(x)

x = 45 / 5
print(x)

x = 56 * 89
print(x)

x = 89 % 7
print(x)

x = 87 ** 78
print(x)

x = 34 // 3
print(x)


# Assignment Operators

x = 97

x = x + 34
print(x)

x = x - 90
print(x)

x = x / 2
print(x)

x = x // 3
print(x)

x = x % 5
print(x)

x = x ** 9
print(x)


# Comparison Operators

x = 9
y = 10

print(x == y)

print(x != y)

print(x > y)

print(x < y)

print(x <= y)

print(x >= y)


# Logical Operators

x = 7
y = 8

print(x > y and x < y)

print(x > y or x < y)

print(not(x > y))


# Identity Operators

x = 10
y = 10

print(x is y)

print(x is not y)
