"""
Task 1
Generate a string, whose length is in [8, 20], containing at least one upper case, one lower case, one number and one symbol.
Consider Python’s string and random module.
Print the string
You need 1 or 2 player(s)
"""
import random

MIN_LENGTH = 8
MAX_LENGTH = 20
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def generate_password():
    password = ''
    password_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    # Add in most lowercase letters
    for character in range(password_length - 2):
        password += (random.choice(LOWER))
    # Add in one Upper case letter and one special character
    password += (random.choice(UPPER))
    password += (random.choice(SPECIAL_CHARACTERS))


generate_password()
# print(password)
