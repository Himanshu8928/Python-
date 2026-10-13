#Write a program to perform slicing, basic and advanced indexing on NumPy arrays.

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Slicing
print("Slicing:", arr[1:4])
print("First three elements:", arr[:3])

# Basic Indexing
print("Element at index 0:", arr[0])
print("Element at index 3:", arr[3])

# Advanced Indexing
print("Selected elements:", arr[[0, 2, 4]])

# Boolean Indexing
print("Elements greater than 30:", arr[arr > 30])

#Write a program to analyze dimensions and attributes of arrays.

import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Array:")
print(arr)

print("Number of Dimensions:", arr.ndim)
print("Shape of Array:", arr.shape)
print("Size of Array:", arr.size)
print("Data Type:", arr.dtype)

