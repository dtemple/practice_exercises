# Take two lists, say for example these two:
#
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

# NOTE: Could not figure this out as it requires sets

import random
a = random.sample(range(1,15),8)
b = random.sample(range(1,15),9)

c=[]

for x in a:
    if x in b and x not in c:
        c.append(x)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [x for x in a if x in b]
d = [x for x in a if x in b]

e = [x for x in c for y in d if x != y]

print(e)

print(a)
print(b)