#Write a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 2026 + (100 - age)

print(name, "you will turn 100 years old in the year", year)

#Write a program to accept a number from the user and depending on whether the number is even or odd,
#print out an appropriate message to the user.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a program to accept the SGPI from the user and print corresponding grade.
sgpi = float(input("Enter your SGPI: "))

if sgpi >= 9.00 and sgpi <= 10.00:
    print("Grade: O")
elif sgpi >= 8.00:
    print("Grade: A+")
elif sgpi >= 7.00:
    print("Grade: A")
elif sgpi >= 6.00:
    print("Grade: B+")
elif sgpi >= 5.50:
    print("Grade: B")
elif sgpi >= 5.00:
    print("Grade: C")
elif sgpi >= 4.00:
    print("Grade: P")
elif sgpi >= 0:
    print("Grade: F")
else:
    print("Invalid SGPI")

