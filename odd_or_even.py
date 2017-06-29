# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Please input a number: "))
check = int(input("Input one more: "))

def checknum(num):
    print("First I'll check if the first a multiple of 4, if it's even or if it's odd: ")
    if num % 4 == 0:
        print("it's a multiple of 4 \n")
    elif num % 2 == 0:
        print("it's even \n")
    else:
        print("it's odd \n")

checknum(num)

def divisable(num,check):
    print("Now I'll check if the first is divisable by the second: ")
    if num % check == 0:
        print("yup, it is")
    else: print("nope")

divisable(num, check)