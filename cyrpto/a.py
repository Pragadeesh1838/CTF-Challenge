cipher = open("backup.enc", "rb").read()

# Use longer known plaintext
known = b"SECE{xor_"   # 9 bytes, longer than key

# Recover key
key = bytearray(cipher[i] ^ known[i] for i in range(6))

print("Recovered key:", key.decode())

# Decrypt full message
flag = bytes(cipher[i] ^ key[i % len(key)] for i in range(len(cipher)))
print("Flag:", flag.decode())
