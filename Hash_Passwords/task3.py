"""Task 3. Use the hashed password function when loading new passwords"""

import hashlib
import string
import random

LENGTH = 15  # Set the required length of salt

# Declaring Password - remove this when implementing as password is declared in Task 1.
password = 'GeeksPassword'

# Generate pseudorandom aplhanumerical string as salt
# ascii_letters consist of alphabets for 'a' to 'z' and 'A' to 'Z'
# digits consist of '0' to '9'
characters = string.ascii_letters + string.digits
# generated_string = ''.join(random.choice(characters) for _ in range(length))
# If you want to avoid using loops then choices is a better option
salt = ''.join(random.choices(characters, k=LENGTH))

# Adding salt at the last of the password.
salty_password = password + salt
# Encoding the password.
hashed = hashlib.md5(salty_password.encode())

# Printing the Hash.
print(hashed.hexdigest())
