# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
#  lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password
#  every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

length = 0
pw=[]
x=list(range(1,10))
print(x)

def choose_type():
    type=random.randint(1,4)
    #print("type chosen is " + type)
    return type

def choose_character():
    type=choose_type()
    random_integer = str(random.randint(1, 9))
    random_lowercase = random.choice('abcdefghijklmnopqrstuvwxyz')
    random_uppercase = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random_symbol = random.choice('!@#$%^&*()_+=-')
    if type == 1:
        return random_integer
    elif type == 2:
        return random_lowercase
    elif type == 3:
        return random_uppercase
    elif type == 4:
        return random_symbol
    else:
        print("Something went wrong.")

def choose_word():
    wc=random.randint(1,3)
    easy_passwords=["easy","password","guessable","simplepw"]
    return easy_passwords[wc]

choice= input("Welcome to the password generator. \n Would you like a strong password or a weak one that is easier to remember? (strong/weak)")

if choice == "strong":
    for a in x:
        ch = choose_character()
        pw.append(ch)
    result = "".join(pw)
    print("Here is your password: " + result)
elif choice == "weak":
    word=choose_word()
    print("Your password is: " + word)
else: print("Please type strong or weak")