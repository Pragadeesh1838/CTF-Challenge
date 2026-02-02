cipher = open("backup.enc", "rb").read()
known = b"SECE{"

key_len = 6
key = bytearray(key_len)

# Recover known part of key
for i in range(len(known)):
    key[i] = cipher[i] ^ known[i]

# Recover the last key byte using printability
for k in range(32, 127):
    test_key = key[:]
    test_key[5] = k

    decrypted = bytes(cipher[i] ^ test_key[i % key_len] for i in range(len(cipher)))

    if decrypted.startswith(b"SECE{") and decrypted.endswith(b"}"):
        print("Recovered key:", test_key.decode())
        print("Flag:", decrypted.decode())
        break

