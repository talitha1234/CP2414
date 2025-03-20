"""
Task 3
Write a string into a file
You need 0.5 player
"""



def write_pw_to_file():
    password = 'GeekPassword'
    password_file = "pwfile"
    in_file = open(password_file, 'w')
    print(password, file=in_file)
    in_file.close()


write_pw_to_file()
