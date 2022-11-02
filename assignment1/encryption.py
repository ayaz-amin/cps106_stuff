# Function to encode data
def encrypt(plain_text, key):
    key_dict = {}
    text_encoded = []
    for i, k in enumerate(key):
        key_dict[i] = k
    for val in plain_text:
        text_encoded.append(
            key_dict[val]
        )
    return bytes(text_encoded)

# Function to decode data
def decrypt(cipher_text, key):
    key_dict = {}
    text_decoded = []
    for i, k in enumerate(key):
        key_dict[k] = i
    for val in cipher_text:
        text_decoded.append(
            key_dict[val]
        )
    return bytes(text_decoded)

# Function to read binary data
def read_file(file_name):
    f = open(file_name, "rb")
    content = f.read()
    f.close()
    return content

# Function to write binary data
def write_file(file_name, content):
    f = open(file_name, "wb")
    f.write(content)
    f.close()

# Main testing function
def test_encryption():
    plain_text = read_file("plain_text")
    key = read_file("key")
    cipher_text = encrypt(plain_text, key)
    write_file("cipher_text", cipher_text)
    cipher_text_opened = read_file("cipher_text")
    decoded = decrypt(cipher_text_opened, key)
    write_file("plain_text1", decoded)

# Entry point
if __name__ == "__main__":
    test_encryption()