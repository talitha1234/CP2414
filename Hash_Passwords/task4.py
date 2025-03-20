"""
Task 4
Generate the salt (random number)
Consider Python’s random.uniform() method
Implement a one-way hash function
Consider Python’s hashlib module
You need 2 or 3 players
"""
import random
import hashlib
import struct

test_password = 'test_passworD#'


def generate_salt():
    salt = struct.pack("d", random.uniform(0, 1))
    salt_string = str(salt)
    return salt_string


def hasher(password, salt_string):
    # Encode password to bytes because that is what hashlib expects
    password_bytes = password.encode()
    salt_bytes = salt_string.encode()
    # Generate a random float and convert it to 8-byte representation

    hash_function = hashlib.new("sha256")
    #
    hash_function.update(salt_bytes + password_bytes)
    # Get the final hashed password -  converts the hash output (in bytes) to a readable hexadecimal string
    hashed_password = hash_function.hexdigest()
    print("Hashed Password: " + hashed_password)
    return hashed_password


# hasher(test_password)
