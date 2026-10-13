#Write a program that takes two lists and returns True if they have at least one common member.

def common_member(list1, list2):
    for x in list1:
        if x in list2:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(common_member(list1, list2))

# Write a Python script to sort (ascending and descending) a dictionary by value

d = {'a': 5, 'b': 2, 'c': 8, 'd': 1}

print("Original Dictionary:", d)

# Ascending Order
asc = dict(sorted(d.items(), key=lambda x: x[1]))
print("Ascending Order:", asc)

# Descending Order
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
print("Descending Order:", desc)
