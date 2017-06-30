# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in
# the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
#  is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

import sys

def check_zero(num):
    if num == 0:
        sys.exit("Ok! Not printing anything.")
    else:
        return

def gen_fib():
    base_num = 1
    prev_nums = []
    cycles = 0
    while cycles < num:
        if cycles == 0:
            prev_nums.append(base_num)
            cycles += 1
        else:
            x = len(prev_nums) - 1
            y = prev_nums[x]
            z = y + x
            prev_nums.append(z)
            cycles += 1
    return prev_nums

num = int(input("How many fibonnaci numbers would you like to generate? "))

check_zero(num)
x = gen_fib()

print(x)