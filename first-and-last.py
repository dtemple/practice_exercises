# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes
# a new list of only the first and last elements of the given list. For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

d = []

first = a[0]
c = int(len(a))-1
last = a[c]

d = [first,last]