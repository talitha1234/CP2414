# code taken from past class, adjusting for task
from token import NUMBER

# Task 2
# Read inputs from keyboard typing
# Consider Python’s input() method/function
# Check a string’s length and whether contains upper case, lower case, number and symbol
# Consider Python’s len() method
# You check Regular Expressions (regex), consider Python’s re module
# You need 2 or 3 players

MIN_LENGTH = 2
MAX_LENGTH = 14
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
NUMBER_CHARACTERS = "0123456789"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:", SPECIAL_CHARACTERS)

    password = input("> ")

    is_valid_password(password)


def is_valid_password(password):
    """Determine if the provided password is valid."""

    secure = True
    while secure:
        length = len(password)

        if length < MIN_LENGTH or length > MAX_LENGTH:
            print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH)
            break

        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
            if char.isupper():
                count_upper += 1
            if char.islower():
                count_lower += 1
            if char in NUMBER_CHARACTERS:
                count_digit += 1

        if count_upper & count_lower & count_digit & count_special >= 1:
            print('vaild password')
            return True
        else:
            print("Invalid Password")
            return False




if __name__ == "__main__":
    main()
