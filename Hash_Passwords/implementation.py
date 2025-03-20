"""
Demo of all tasks - User inputs a password and it is hashed
"""

from task1 import generate_password
from task2 import is_valid_password
# from task3 import write_pw_to_file
from task4 import hasher, generate_salt


def main():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if is_valid_password(password):
        print("get to this line")
        salt = generate_salt()
        hashed_password = hasher(password, salt)
        write_pw_to_file(username, hashed_password, salt)
        # TODO: get user to enter username and password again and verify
        #  this by comparing the stored (in file pwfile) username, hashed password and salt

# couldn't get the below function to run from importing so I've copied it here
def write_pw_to_file(username, hashed_password, salt):
    password_file = "pwfile"
    in_file = open(password_file, 'w')
    print(username + '\n' + hashed_password + '\n' + salt, file=in_file)
    in_file.close()


main()
