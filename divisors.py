# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input("Please input a number. I'll output a list of divisors. "))

numlist = range(1,num)

output = []

for x in numlist:
    if num % x == 0:
        output.append(x)

print(output)