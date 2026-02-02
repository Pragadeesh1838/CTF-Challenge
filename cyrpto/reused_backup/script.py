flag = b"SECE{xor_is_not_encryption}"
key  = b"crypto"

cipher = bytes([flag[i] ^ key[i % len(key)] for i in range(len(flag))])
print(cipher.hex())
