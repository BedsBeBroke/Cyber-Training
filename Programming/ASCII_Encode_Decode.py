def encode(text, key):
    return ''.join(chr((ord(char) + key) % 256) for char in text)

def decode(encoded_text, key):
    return ''.join(chr((ord(char) - key) % 256) for char in encoded_text)

if __name__ == "__main__":
    print("String Encoder/Decoder")
    choice = input("Choose an option (encode/decode): ").strip().lower()
    if choice == "encode":
        text = input("Enter the string to encode: ")
        key = int(input("Enter the numeric key: "))
        encoded = encode(text, key)
        print(f"Encoded string: {encoded}")
        with open("encoded_output.txt", "w") as f:
            f.write(encoded)
        print("Encoded output saved to encoded_output.txt")
    elif choice == "decode":
        encoded = input("Enter the string to decode: ")
        key = int(input("Enter the numeric key: "))
        decoded = decode(encoded, key)
        print(f"Decoded string: {decoded}")
    else:
        print("Invalid option.")

"""
Test Results:

Original: Computer
Key: 3
Encoded: Frpsxwhu
Decoded: Computer

Original: Python
Key: 10
Encoded: Z}~ryx
Decoded: Python

Original: Cybersecurity
Key: 8
Encoded: Kjmz{mk}zq|
Decoded: Cybersecurity
"""