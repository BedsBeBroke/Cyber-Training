from pwn import xor

xor_string = '686974207468652062756c6c277320657965'          # hex string
byte_string = bytes.fromhex('1c0111001f010100061a024b53535009181c')  # bytes

# Make sure both args are bytes, then call .hex() on the result
xor_byte_string = xor(byte_string, bytes.fromhex(xor_string))
final_string = xor_byte_string.hex()
print(final_string)   # -> 746865206b696420646f6e277420706c6179