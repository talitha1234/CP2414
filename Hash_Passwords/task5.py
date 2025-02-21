"""
Task 5
Read a string (password) from the keyboard input
Call your hash function to verify the password
You need 0.5 player
"""

import random
import hashlib
import struct

test_password = input("Enter password: ")


def hasher(password):
    password_bytes = password.encode() # Encodes test password into bytes that a hash can work with.
    hash_function = hashlib.new("sha256") # Create a new 256 hash.
    hash_function.update(stored_salt + password_bytes) # Mix/merge both salt and passwords.
    hashed_password = hash_function.hexdigest() # Digests the binary hash into hexdec.
    print("Hashed Password: " + hashed_password) #Show off the hash to show it's working.
    return hashed_password


stored_salt = struct.pack("d", random.uniform(0, 1)) # Gnerates a random floating-point number between 0 and 1, then converts said random number into binary.
stored_hash = hasher(test_password) # Uses the function to hash tf out of the test password.

input_password = input("What's the password?: ")
if hasher(input_password) == stored_hash: # Hashes tf out of the inputted password, then checks if it's the same.
    print("Password verified.")
else:
    print("Incorrect password.") # How???
