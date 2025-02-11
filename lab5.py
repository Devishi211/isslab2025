def rail_fence_encrypt(text, rails):
    rail = [['\n' for _ in range(len(text))] for _ in range(rails)]
    
    direction_down = False
    row, col = 0, 0

    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        
        rail[row][col] = char
        col += 1
        row += 1 if direction_down else -1

    ciphertext = ''.join([''.join(row) for row in rail if row])
    return ciphertext.replace('\n', '')

def rail_fence_decrypt(ciphertext, rails):
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    direction_down = None
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*' and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        
        result.append(rail[row][col])
        col += 1
        row += 1 if direction_down else -1

    return "".join(result)

#mainfunction
plaintext = "HELLO WORLD".replace(" ", "") 
rails = 3


ciphertext = rail_fence_encrypt(plaintext, rails)
print("\nEncrypted Text:", ciphertext)
decrypted_text = rail_fence_decrypt(ciphertext, rails)
print("Decrypted Text:", decrypted_text)
