#Write a program to perform basic operations, indexing and slicing on arrays.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# Basic Operations
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# Indexing
print("Element at index 0:", arr[0])
print("Element at index 2:", arr[2])

# Slicing
print("Elements from index 1 to 3:", arr[1:4])
print("First three elements:", arr[:3])
print("Last two elements:", arr[-2:])

# Write a program to implement mathematical functions on arrays.

import numpy as np

arr = np.array([1, 4, 9, 16, 25])

print("Original Array:", arr)
print("Square Root:", np.sqrt(arr))
print("Square:", np.square(arr))
print("Exponential:", np.exp(arr))
print("Logarithm:", np.log(arr))
print("Sum:", np.sum(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))

#Write a program to perform array aliasing and copying.

import numpy as np

# Original array
a = np.array([10, 20, 30, 40, 50])
print("Original Array:", a)

# Array Aliasing
b = a
b[0] = 100
print("After Aliasing, a:", a)
print("After Aliasing, b:", b)

# Array Copying
c = a.copy()
c[1] = 200
print("After Copying, a:", a)
print("After Copying, c:", c)












