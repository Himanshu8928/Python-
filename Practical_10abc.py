#Write a program that compares two dates (in DD/MM/YYYY format) and prints which one is earlier.

from datetime import datetime

date1 = input("Enter first date (DD/MM/YYYY): ")
date2 = input("Enter second date (DD/MM/YYYY): ")

d1 = datetime.strptime(date1, "%d/%m/%Y")
d2 = datetime.strptime(date2, "%d/%m/%Y")

if d1 < d2:
    print("First date is earlier.")
elif d2 < d1:
    print("Second date is earlier.")
else:
    print("Both dates are equal.")

#Write a program to measure program execution time.

import time

start = time.time()

# Program to calculate the sum of numbers
total = 0
for i in range(1, 1000001):
    total = total + i

end = time.time()

print("Sum =", total)
print("Execution time:", end - start, "seconds")

#Write a program using the calendar module to print
#the weekday of the first day of a given month and year.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

weekday = calendar.weekday(year, month, 1)
day_name = calendar.day_name[weekday]

print("The first day of the month is:", day_name)









    
