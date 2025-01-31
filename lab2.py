def construct_playfair_matrix(key: str) -> list:


    matrix = []
    key = key.upper().replace('J', 'I')
    seen = set()
    for char in key:
        if char not in seen and char.isalpha():
            matrix.append(char)
            seen.add(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]
def find_position(matrix, char):


    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return -1, -1
def playfair_cipher(text, key, encrypt=True):


    matrix = construct_playfair_matrix(key)
    text = text.upper().replace('J', 'I')
    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            b = 'X'
        else:
            i += 1
        digraphs.append((a, b))
        i += 1
    result = ""
    for a, b in digraphs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            if encrypt:
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if encrypt:
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result
if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "BALLOON"
    ciphertext = playfair_cipher(plaintext, key, encrypt=True)
    print("Ciphertext:", ciphertext)
    print("Decrypted:", playfair_cipher(ciphertext, key, encrypt=False))
