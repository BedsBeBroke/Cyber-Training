#!/usr/bin/env python3
# Decrypt 7.txt (base64 + AES-128-ECB) using PyCryptodome
#!/usr/bin/env python3
import base64
from Crypto.Cipher import AES

key = b'YELLOW SUBMARINE'

b64 = open('7.txt').read()
ct = base64.b64decode(b64)

cipher = AES.new(key, AES.MODE_ECB)
pt = cipher.decrypt(ct)

pad = pt[-1]
if 1 <= pad <= 16 and pt[-pad:] == bytes([pad]) * pad:
    pt = pt[:-pad]

text = pt.decode('utf-8', errors='replace')
print(text)

open('7.dec.txt', 'w').write(text)
print(text)
