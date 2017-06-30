# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


a = [1, 1, 2, 3, 5, 8, 8, 21, 34, 55, 89]

# Using a set
b = set(a)
newlist = list(b)

print(newlist)

# Set + function
def remove_dupes(x):
    b = set(x)
    newlist = list(b)
    return newlist

print(remove_dupes(a))

# Or using a for loop
b = []

for x in a:
    if x not in b:
        b.append(x)
''' b = [x for x in a if x not in b] Doesn't work not sure why'''


# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = a+b
d=set(c)
newlist=list(d)
print(newlist)

# One line
c = [x for x in set(a) if x in set(b)]