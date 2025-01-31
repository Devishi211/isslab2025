import numpy as np
from string import ascii_uppercase

def text_to_numbers(text):
    return [ascii_uppercase.index(c) for c in text]

def numbers_to_text(numbers):
    return ''.join(ascii_uppercase[n % 26] for n in numbers)

def prepare_text(text, size):
    text = text.upper().replace(" ", "")
    while len(text) % size:
        text += "X"
    return text

def encrypt(plain, key):
    size = len(key)
    plain = prepare_text(plain, size)
    key_matrix = np.array(key)
    cipher_text = ""
    for i in range(0, len(plain), size):
        block = np.array(text_to_numbers(plain[i:i+size]))
        cipher_block = np.dot(key_matrix, block) % 26
        cipher_text += numbers_to_text(cipher_block)
    return cipher_text

def decrypt(cipher, key):
    size = len(key)
    key_matrix = np.array(key)
    inv_key = np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)
    inv_key = np.round(inv_key * pow(int(np.linalg.det(key_matrix)), -1, 26)) % 26
    inv_key = inv_key.astype(int)
    plain_text = ""
    for i in range(0, len(cipher), size):
        block = np.array(text_to_numbers(cipher[i:i+size]))
        plain_block = np.dot(inv_key, block) % 26
        plain_text += numbers_to_text(plain_block)
    return plain_text

key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
plain_text = "HELLO"
cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)

print("Cipher:", cipher_text)
print("Decrypted:", decrypted_text)