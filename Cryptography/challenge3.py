cipher_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
data = bytes.fromhex(cipher_hex)

best_score = -1
best_key = None
best_plain = None

for key in range(256):
    plain = bytes([b ^ key for b in data])
    text = plain.decode('ascii', errors='ignore')
    s = 0
    for ch in text.lower():
        if ch == ' ':
            s += 3
        elif ch in 'etaoinshrdlu':
            s += 1
    if s > best_score:
        best_score = s
        best_key = key
        best_plain = text

print(best_key)
print(best_plain)
