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


def hasher(password):
    # Encode password to bytes because that is what hashlib expects
    password_bytes = password.encode()
    # Generate a random float and convert it to 8-byte representation
    salt = struct.pack("d", random.uniform(0, 1))
    hash_function = hashlib.new("sha256")
    #
    hash_function.update(salt + password_bytes)
    # Get the final hashed password -  converts the hash output (in bytes) to a readable hexadecimal string
    hashed_password = hash_function.hexdigest()
    print("Hashed Password: " + hashed_password)


hasher(test_password)
