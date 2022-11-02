# -*- coding: utf-8 -*-
"""
Permutation encryption scheme
In a permutation scheme, messages are encrypted by permuting the bytes that represent the message.
For example, a permutation of the word “hello”, which is a sequence of 5 bytes representing the
letters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’, is “loelh”. To explain how the permutation encryption works, let us run a toy
example. Assume that all messages consist of only the letters a, b, c, d, and assume these letters are
given in the fixed order (a, b, c, d) which means ‘a’ is in the first place, ‘b’ is in the second place, and
so on. In the encryption scheme an example key would be K = bdca. This key represents a
permutation of the above order. For encryption and decryption, K represents a map:
(a, b, c, d) -> (b, d, c, a).
Suppose we are given the message M = “ddcacbdccaa” which we refer to as plaintext. To encrypt M
using the K we simply replace ‘a’ by ‘b’, ‘b’ by ‘d’, ‘c’ by ‘c’ (so no change for ‘c’), and ‘d’ by ‘a’. The
encrypted message, which we refer to as ciphertext, is then C = “aacbcdaccbb”. To decrypt C, we
consider the inverse of the above mapping, that is 
(a, b, c, d) -> (d, a, c, b).
This mapping is easily computed using K, so that we are able to encrypt and decrypt using the same
key.
Implementation
To be able to encrypt any given message, you need to consider every possible value of a byte. The
value of a byte is in the range [0, 255], so the keys are always 256 byte long. The default order in a
key is the usual numerical order: (0, 1, 2, ..., 255). Therefore, an example key (251, 24, 31, ..., 186)
represents the mapping (0, 1, 2, ..., 255) -> (251, 24, 31, ..., 186), i.e., 0 is mapped to 251, 1 is mapped to
24, etc. Write a python file named encryption.py that contains the following functions:

"""




"""
Accepts a plaintext and a key, and returns a ciphertext that is the encryption of the plaintext using
the input key. The plaintext is a list of bytes of arbitrary length, and key is a list of bytes of length
256.
"""
def encrypt(plain_text, key):
    cipher_text=[]
    key_dict=[]
    position=0
    for i in key:
        key_dict.append((position,i))
        position+=1
    for enc in plain_text:
        for i, j in key_dict:
            if i==enc:
                cipher_text.append(j)
        #cipher_text.append(key_dict[enc])
    return bytes(cipher_text)

"""
    for i in range(len(plain_text)):
        #mapped=(map(str(key),str(plain_text)))
        #mapped=[*map(key,plain_text)]
        #cipher_text.append(str(mapped))
        #cipher_text=mapped
        cipher_text.append(key_dict[plain_text[i]])
    return cipher_text
"""
 
"""
Accepts a ciphertext and a key, and returns a plaintext that is the decryption of the ciphertext using
the input key. The cyphertext is a list of bytes of arbitrary length, and key is a list of bytes of length
256.  
"""
def decrypt(cipher_text, key):
    plain_text1=[]
    key_dict=[]
    position=0
    for i in key:
        key_dict.append((position,i))
        position+=1
    for enc in cipher_text:
        for i, j in key_dict:
            if j==enc:
                plain_text1.append(i)
        #cipher_text.append(key_dict[enc])
    return bytes(plain_text1)
    
    
    """
    plain_text1=[]
    for i in range(len(cipher_text)):
        #mapped_c=(map(str(key),str(cipher_text)))
        #mapped_c=map(key,cipher_text)
        #plain_text1=mapped_c
        key1=list(reversed(key))
        plain_text1.append(key1[cipher_text[i]])
        
    return plain_text1
"""



"""
Accepts a filename and returns the content of the file as a list of bytes. For this, you need to open the
file in binary mode.
"""
def read_file(file_name):
    file = open(file_name, "rb")
    content = file.read()
    file.close()
    return content


"""
Accepts a filename and a content, and writes the content to the file. For this, you need to open the file
in binary mode. Use the python built-in function bytes to convert the content to a list of bytes
before writing it to the file.
"""
def write_file(file_name, content):
    new_file=open(file_name,'wb')
    #content_bytes=bytes((content))
    #file.write(content_bytes)
    new_file.write(bytes(content))
    new_file.close()
    return new_file
    
    
    
    
"""
To test your encryption and decryption, write the following function:
    In this function, you performs the following steps: 
1. Read the key from a file named “key”. (use the read_file function)
2. Encrypt the content of a file named “plain_text”. (use read_file and encrypt)
3. Write the ciphertext from Step 2 to a file called “cipher_text”. (use write_file)
4. Decrypt the ciphertext from the file “cipher_text” that was created in Step 3. (use read_file
and decrypt)
5. Write the plaintext from Step 4 to a file called “plain_text1”. (use write_file)
If the files “plain_text1” and “plain_text” are the same then your algorithms work correctly.
"""
def test_encryption():
    #Step 1
    key=read_file('key')
    #print(key)
    
    #Step 2
    plain_text=read_file('plain_text')
    #print(plain_text)
    encryption=encrypt(plain_text, key)
    #print(encryption)
    
    #Step 3
    write_file('cipher_text', encryption)
    #print(read_file('cipher_text'))
    
    #Step 4
    cipher_text=read_file('cipher_text')
    #print(cipher_text)
    decryption=decrypt(cipher_text, key)
    #print(decryption)
    
    #Step 5
    write_file('plain_text1', decryption)
    return read_file('plain_text1')

#print(test_encryption())
#print(read_file('plain_text'))
print(test_encryption()==(read_file('plain_text')))
#print(read_file('key'))
    
    
    
    
    
    