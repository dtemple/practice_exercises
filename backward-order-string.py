#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order.

def get_input(help_text="Please enter a short sentence: "):
    user_input = input(help_text)
    return user_input

def reverse_words(user_input):
    words = user_input.split()
    rvs = words[::-1]
    output = " ".join(rvs)
    return output

user_input=get_input()
output=reverse_words(user_input)

print(output)