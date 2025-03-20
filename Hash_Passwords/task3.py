"""
Task 3
Write a string into a file
You need 0.5 player
"""


def main():
    username = "JC261777"
    hashed_password = 'GeekPassword'
    salt = "123"

    write_pw_to_file(username, hashed_password, salt)


def write_pw_to_file(username, hashed_password, salt):
    password_file = "pwfile"
    in_file = open(password_file, 'w')
    print(username + '\n' + hashed_password + '\n' + salt, file=in_file)
    in_file.close()


if __name__ == "__main__":
    main()

