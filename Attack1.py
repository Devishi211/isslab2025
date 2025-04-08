from string import ascii_letters  # includes a-z and A-Z
from time import time_ns
import random

# Character set includes A-Z, a-z, and space
charset = ascii_letters + ' '

# Actual secret (plaintext)
secret = 'devi'

# Simulated comparison function (vulnerable)
def comp(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            return False
        # Artificial delay to increase timing difference
        for _ in range(20000): pass
    return True

# Login function using the vulnerable comparison
def login(user_input):
    if comp(secret, user_input):
        return 'Access Granted'
    return 'Access Denied'

# Guess one character at a time
def cracked_letter(cracked, padding):
    timings = {ch: 0 for ch in charset}
    for _ in range(100):  # Reduce a bit to make testing faster
        for ch in charset:
            guess = cracked + ch + '-' * padding
            start = time_ns()
            login(guess)
            end = time_ns()
            timings[ch] += end - start
    # Return character with highest timing (most correct so far)
    return max(timings, key=timings.get)

# Main cracking loop
target_length = len(secret)
cracked = ''
padding = target_length - 1

for _ in range(target_length):
    next_char = cracked_letter(cracked, padding)
    cracked += next_char
    padding -= 1
    print(f"Guessed so far: {cracked}")

print(f"\n Final guessed plaintext: {cracked}")


