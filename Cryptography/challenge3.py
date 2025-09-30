cipher_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

data = bytes.fromhex(cipher_hex)

def score(text: str):
    text = text.lower()
    score = 0
    for ch in text:
        if ch == ' ':
            score += 3
        elif ch in 'etaoinshrdlu':
            score += 1
    return score

best_score = -1
best_key = None
best_plain = None

for key in range(256):
    plain_bytes = bytes([b ^ key for b in data])

    if ((b < 32 and b != 10) or b > 126 for b in plain_bytes):
        continue

    try:
        plain_text = plain_bytes.decode('ascii')
    except UnicodeDecodeError:
        continue

    s = score(plain_text)
    if s > best_score:
        best_score = s
        best_key = key
        best_plain = plain_text

if best_plain is not None:
    print('Best key:', best_key)
    print('Plaintext:')
    print(best_plain)
