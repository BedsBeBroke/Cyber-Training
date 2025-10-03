from pathlib import Path
from collections import Counter

def detect_ecb(file_path):
    p = Path(file_path)
    lines = [l.strip() for l in p.read_text().splitlines() if l.strip()]
    best = None
    for i, h in enumerate(lines, start=1):
        try:
            b = bytes.fromhex(h)
        except Exception:
            continue
        blocks = [b[j:j+16] for j in range(0, len(b), 16)]
        cnt = Counter(blocks)
        repeats = sum(v-1 for v in cnt.values() if v>1)
        if repeats and (best is None or repeats > best[0]):
            best = (repeats, i, h, [blk.hex() for blk, v in cnt.items() if v>1])
    return best

if __name__ == '__main__':
    res = detect_ecb('8.txt')
    if not res:
        print('No ECB-like ciphertext found')
    else:
        repeats, line_no, hexline, repeated_blocks = res
        print(f'Line {line_no} has {repeats} repeated 16-byte block(s)')
        print('Repeated block(s):')
        for b in repeated_blocks:
            print(b)