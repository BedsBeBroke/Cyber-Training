from pwn import xor

xor_string = bytes.fromhex('686974207468652062756c6c277320657965')
byte_string = bytes.fromhex('1c0111001f010100061a024b53535009181c')

xor_byte_string = xor(byte_string, xor_string)
final_string = xor_byte_string.hex()
print(final_string)
