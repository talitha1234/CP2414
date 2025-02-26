Finish Week3 and Week4’s work
• Week 3: No need to implement the hash function yourself, just call the
Python library – hashlib
• Week 4: Replace your Week 3’s hash with Caesar cipher and DES
• Implement Caesar yourself
• Call Python library - PyCryptodome for DES

This week (groups of three):
• Implement the secret value-based hash function by yourself
• You may also call any existing hash function (taking only one input – message), e.g.,
SHA-512
• The secret value should be random with a given length (think about the maximum
length in line with the accepted length of the hash function)
• Note: the secret value is shared by the user and the server!
• Call Python Library to implement RSA then Replace DES with RSA
• There is a Python library for RSA
• Install: pip install rsa
• Documentation: read and self-taught



Accept users registration
Provide options for computer-generated passwords (Task 1)
Proactively check users’ own passwords (Task 2)
Lower case + Upper case + numbers + symbols + at least 8 characters
Use the hashed password function when loading new passwords (Task 3)
Save the hashed password to a password file (Task 4)
Verify users’ authentication for log-in attempts (Task 5)
Use the hashed password function to verify

Task 1
Generate a string, whose length is in [8, 20], containing at least one upper case, one lower case, one number and one symbol.
Consider Python’s string and random module.
Print the string
You need 1 or 2 player(s)

Task 2
Read inputs from keyboard typing
Consider Python’s input() method/function
Check a string’s length and whether contains upper case, lower case, number and symbol
Consider Python’s len() method
You check Regular Expressions (regex), consider Python’s re module
You need 2 or 3 players

Task 3
Write a string into a file
You need 0.5 player
    
Task 4
Generate the salt (random number)
Consider Python’s random.uniform() method
Implement a one-way hash function
Consider Python’s hashlib module
You need 2 or 3 players

Task 5
Read a string (password) from the keyboard input
Call your hash function to verify the password
You need 0.5 player
