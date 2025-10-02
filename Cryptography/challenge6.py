import base64
from collections import Counter

ct_b64 = open('6.txt').read()
ct = base64.b64decode(ct_b64)


def hamming(a: bytes, b: bytes) -> int:
    assert len(a) == len(b)
    dist = 0
    for x, y in zip(a, b):
        v = x ^ y
        # count bits in v
        dist += bin(v).count('1')
    return dist

COMMON = set(' etaoinshrdlu')
def score_text(s: str) -> int:
    s = s.lower()
    sc = 0
    for ch in s:
        if ch in COMMON:
            sc += 1
    return sc

def solve_single_byte_xor(data: bytes):
    best = None
    for key in range(256):
        pt = bytes([b ^ key for b in data])
        try:
            text = pt.decode('ascii')
        except UnicodeDecodeError:
            continue
        sc = score_text(text)
        if best is None or sc > best[0]:
            best = (sc, key, text)
    return best

KEYSIZE_CANDIDATES = []
for ks in range(2, 41):
    blocks = [ct[i:i+ks] for i in range(0, ks*4, ks)]
    if len(blocks[-1]) < ks:
        continue
    dists = []
    for i in range(3):
        dists.append(hamming(blocks[i], blocks[i+1]) / ks)
    avg = sum(dists) / len(dists)
    KEYSIZE_CANDIDATES.append((avg, ks))

KEYSIZE_CANDIDATES.sort()
candidates = [ks for _, ks in KEYSIZE_CANDIDATES[:3]]

final_results = []
for ks in candidates:
    blocks = [ct[i:i+ks] for i in range(0, len(ct), ks)]
    transposed = []
    for i in range(ks):
        b = bytearray()
        for block in blocks:
            if i < len(block):
                b.append(block[i])
        transposed.append(bytes(b))
    key_bytes = []
    plain_blocks = []
    for t in transposed:
        res = solve_single_byte_xor(t)
        if res is None:
            key_bytes.append(0)
            plain_blocks.append('')
        else:
            _, k, text = res
            key_bytes.append(k)
            plain_blocks.append(text)
    key = bytes(key_bytes)
    plaintext = ''.join(chr(b ^ key[i % len(key)]) for i, b in enumerate(ct))
    final_results.append((score_text(plaintext), ks, key, plaintext))
final_results.sort(reverse=True)
best = final_results[0]
_, best_ks, best_key, best_plain = best
print('KEYSIZE:', best_ks)
print('KEY:', best_key)
print('\nPLAINTEXT:\n')
print(best_plain)
