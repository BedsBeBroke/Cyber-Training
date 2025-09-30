import base64
decoded = bytes.fromhex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
base64_bytes = base64.b64encode(decoded)
base64_string = base64_bytes.decode('utf-8')
print({base64_string})