# Small Subgroup Confinement Attack Simulation

p = 23           # Prime modulus
g = 5            # Generator
a = 6            # Victim's private key (unknown to attacker)

# Victim's public key (normal DH step)
A = pow(g, a, p)

# Attacker sends malicious public key in subgroup of order 2
malicious_pub = 22  # 22^2 % 23 == 1

# Victim computes shared secret with attacker's key
s = pow(malicious_pub, a, p)  # Only two possible outcomes: 1 or 22

# Encrypting plaintext with XOR using shared secret as key
plaintext = "hello"
key = s % 256
ciphertext = [ord(c) ^ key for c in plaintext]

# Attacker brute-forces possible shared secrets
for guess in [1, 22]:
    trial_key = guess % 256
    decrypted = ''.join(chr(c ^ trial_key) for c in ciphertext)
    print(f"Trying key={guess}: {decrypted}")
