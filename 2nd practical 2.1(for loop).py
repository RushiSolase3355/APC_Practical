# for loop problems

# Q) Write Python program to print the natural numbers up to n.

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)

# -------------------------------------------------------------------

# Q) Print even number
n = int(input("Enter n: "))

for i in range(2, n + 1, 2):
    print(i)

# -------------------------------------------------------------------

# Q) Print odd number

n = int(input("Enter n: "))

for i in range(1, n + 1, 2):
    print(i)

# ---------------------------------------------------------------------
# Q) WAPP to print 1,2,4,8,16,32,....N^2

n = int(input("Enter number of terms: "))

a = 1

for i in range(n):
    print(a, end=" ")
    a = a * 2

# ---------------------------------------------------------------------

# Q)WAPP to print the sum of given series : 1 + 1/1! + 1/2! + 1/3!....+1/n!

n = int(input("Enter n: "))

fact = 1
sum = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum =", sum)

# ---------------------------------------------------------------------

# Q) WAPP to check weather the square root of a number is prime or not.
