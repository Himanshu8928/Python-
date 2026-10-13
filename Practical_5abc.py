#Write a function to check the input value is Armstrong and also write the function for Palindrome.

# Function to check Armstrong number
def armstrong(n):
    temp = n
    total = 0
    digits = len(str(n))

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")


# Function to check Palindrome
def palindrome(n):
    if str(n) == str(n)[::-1]:
        print(n, "is a Palindrome")
    else:
        print(n, "is not a Palindrome")


num = int(input("Enter a number: "))

armstrong(num)
palindrome(num)

#Write a recursive function to print the factorial for a given number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))

#Write a lambda function that checks whether a given string starts with a specific character.

string = input("Enter a string: ")
ch = input("Enter a character: ")

check = lambda s, c: s.startswith(c)

if check(string, ch):
    print("String starts with the given character.")
else:
    print("String does not start with the given character.")




    







