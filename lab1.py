def caesar_cypher(string: str, shift: int, decrypt: bool = False) -> str:

    result = str()
    if not decrypt:
        for i in range(len(string)):
            result += chr((ord(string[i]) + shift - 65) % 26 + 65)
    else:
        for i in range(len(string)):
            result += chr((ord(string[i]) - shift - 65) % 26 + 65)
    return result
if __name__ == "__main__":
    shift = 5
    to_enc = "HELLOIAMAWESOME" #CHANGES MADE
    to_dec = "MJQQTNFRFBJXTRJ"
    print(caesar_cypher(to_enc, shift))
    print(caesar_cypher(to_dec, shift, decrypt=True))