lines = open('4.txt').read().splitlines()

best_score = -1
best_line = None
best_key = None
best_plain = None

for i, line in enumerate(lines, start=1):
    line = line.strip()
    if not line:
        continue
    data = bytes.fromhex(line)
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
            best_line = i
            best_key = key
            best_plain = text

print(best_line, best_key)
print(best_plain)
