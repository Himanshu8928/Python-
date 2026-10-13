#a. Write a program to compute number of characters and words in a string.

string = input("Enter a string: ")

characters = len(string)
words = len(string.split())

print("Number of characters:", characters)
print("Number of words:", words)
