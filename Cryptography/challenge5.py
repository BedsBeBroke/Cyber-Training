phrase = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"

result = []
for i in range(len(phrase)):
    res.append(ord(phrase[i]) ^ ord(key[i % len(key)]))

print(bytes(result).hex())
