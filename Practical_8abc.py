#a. Write a program to accept and pass radius to a function that returns area and circumference (using tuple).

import math

def circle(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return (area, circumference)

r = float(input("Enter the radius: "))

area, circumference = circle(r)

print("Area of circle:", area)
print("Circumference of circle:", circumference)

#b. Write a program to perform basic file operations on text files and binary files.

import pickle

# Text File Operations
f = open("sample.txt", "w")
f.write("Hello Python\nWelcome to File Handling")
f.close()

f = open("sample.txt", "r")
print("Text File Content:")
print(f.read())
f.close()

# Binary File Operations
data = [10, 20, 30, 40, 50]

f = open("data.dat", "wb")
pickle.dump(data, f)
f.close()

f = open("data.dat", "rb")
print("Binary File Content:")
print(pickle.load(f))
f.close()

#c. Write a Python program to read last n lines of a file.

n = int(input("Enter the number of last lines to read: "))

f = open("sample.txt", "r")
lines = f.readlines()
f.close()

print("Last", n, "lines of the file:")

for line in lines[-n:]:
    print(line, end="")
