# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

num = int(input("Input a number and I'll tell you if it's prime: "))

pdivisors = range(2,num)

actual_divisors = [x for x in pdivisors if num % x == 0]

if len(actual_divisors) == 0:
    print("Prime bitch")
else:
    print("Not prime. It's divisible by " + str(actual_divisors))