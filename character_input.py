# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
random = int(input("Enter a random number: "))

def get100(age):
    born = (2017 - age)
    year = str(born+100)
    return year

def printrand(random):
    x = "Hi " + name + ", you'll turn 100 years old in " + get100(age) + ". \n"
    print(x*random)

printrand(random)
