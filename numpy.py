import numpy as np

# Program 1: 1D array of 10 integers
a = np.array([10,20,30,40,50,60,70,80,90,100])
print("Array:", a)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Dimensions:", a.ndim)

# Program 2: Arithmetic operations on two arrays
a = np.array([10,20,30,40,50])
b = np.array([2,4,5,8,10])
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)

# Program 3: Maximum, minimum, sum and average
a = np.array([12,25,8,45,32,19,50,7,28,15])
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))

# Program 4: Even and odd numbers
a = np.arange(1,21)
print("Even numbers:", a[a%2==0])
print("Odd numbers:", a[a%2!=0])

# Program 5: Reshape array
a = np.arange(1,13)
print("2 x 6:")
print(a.reshape(2,6))
print("3 x 4:")
print(a.reshape(3,4))
print("4 x 3:")
print(a.reshape(4,3))

# Program 6: Addition of two 3 x 3 matrices
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(a+b)

# Program 7: Matrix multiplication
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(np.dot(a,b))

# Program 8: Transpose of 3 x 4 matrix
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("Original:")
print(a)
print("Transpose:")
print(a.T)

# Program 9: Access rows, column and diagonal
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("First row:", a[0])
print("Last column:", a[:,-1])
print("Diagonal:", np.diag(a))
print("Second row:", a[1])
print("Third row:", a[2])

# Program 10: Sum of rows and columns
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Row sums:", np.sum(a,axis=1))
print("Column sums:", np.sum(a,axis=0))

# Program 11: Array slicing
a = np.arange(1,21)
print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate:", a[::2])
print("Reverse:", a[::-1])

# Program 12: Replace values greater than 50 with 0
a = np.array([25,60,45,80,30,75,10,90,55,40])
a[a>50] = 0
print(a)

# Program 13: Ascending and descending order
a = np.array([45,12,78,23,9,56,34])
print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])

# Program 14: Unique elements
a = np.array([10,20,10,30,20,40,30,50,40])
print(np.unique(a))

# Program 15: Horizontal and vertical concatenation
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("Horizontal:")
print(np.hstack((a,b)))
print("Vertical:")
print(np.vstack((a,b)))

# Program 16: Marks of 10 students
marks = np.array([75,82,68,90,55,78,88,72,95,60])
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))

# Program 17: Class average and marks above average
marks = np.array([65,72,81,55,90,76,84,69,95,61,73,88,79,52,67,91,70,85,63,77])
average = np.mean(marks)
print("Class average:", average)
print("Above average:", marks[marks>average])

# Program 18: 3D array
a = np.arange(1,25).reshape(2,3,4)
print(a)
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Size:", a.size)

# Program 19: Access elements from 3D array
a = np.arange(1,25).reshape(2,3,4)
print("First element:", a[0,0,0])
print("Last element:", a[1,2,3])
print("Element [0,1,2]:", a[0,1,2])
print("Element [1,2,3]:", a[1,2,3])

# Program 20: Sums in 3D array
a = np.arange(1,25).reshape(2,3,4)
print("Total sum:", np.sum(a))
print("Layer sums:", np.sum(a,axis=(1,2)))
print("Row sums:", np.sum(a,axis=1))
print("Column sums:", np.sum(a,axis=2))

# Program 21: Replace values greater than 50 in random 3D array
a = np.random.randint(1,101,(2,3,4))
print("Original:")
print(a)
a[a>50] = 0
print("Updated:")
print(a)

# Program 22: Statistics of random 3D array
a = np.random.randint(1,101,(3,4,5))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Standard deviation:", np.std(a))
print("Variance:", np.var(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))

# Program 23: Flatten a 3D array
a = np.arange(1,25).reshape(2,3,4)
print("Original:")
print(a)
print("Flattened:")
print(a.flatten())

# Program 24: Flatten and calculate statistics
a = np.arange(1,28).reshape(3,3,3)
b = a.flatten()
print("Flattened array:", b)
print("Sum:", np.sum(b))
print("Average:", np.mean(b))
print("Maximum:", np.max(b))
print("Minimum:", np.min(b))

# Program 25: Elements greater than 50, even and less than average
a = np.random.randint(1,101,(3,4,5))
b = a.flatten()
average = np.mean(b)
print("Original:")
print(a)
print("Greater than 50:", b[b>50])
print("Even elements:", b[b%2==0])
print("Less than average:", b[b<average])
