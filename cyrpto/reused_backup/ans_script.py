cipher = bytes.fromhex(
    "30373a350f170c00261907300d1d0d2f11010000000000060c1c04"
)

known = b"SECE{"

# Recover key bytes
key_part = bytes([cipher[i] ^ known[i] for i in range(len(known))])
print("Recovered key part:", key_part)

# Guess full key (you know it as creator)
key = b"crypto"

plaintext = bytes([cipher[i] ^ key[i % len(key)] for i in range(len(cipher))])
print("Decrypted:", plaintext)
