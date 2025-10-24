'''
Simple Stream Cypher Demo Code (Symmetric)
Code below take user input to perform encryption and decryption with XOR function.
The cypher key that used will be randomly generated for each input.
'''
# import libraries
import random
import string
# function to generate random key
def gen_ran_key():
    ran_key = random.randint(1, 255)
    return ran_key
# function to encrypt plain text
def encrypt(plain_text, key):
    print(f"encrypt plain text with key equal to {key} (binary: {format(key, '08b')})")
    encrypted_chars = []
    # encrypt the text character by character
    for char in plain_text:
        encrypted = ord(char) ^ key # convert character in text into unicode and perform XOR function with key
        encrypted_chars.append(chr(encrypted)) # returns the character that represents the specified unicode(result) and put into list
    cypher_text = ''.join(encrypted_chars) # make become a string
    return cypher_text
# function to decrypt cypher text
def decrypt(cypher_text, key):
    print(f"decrypt cypher text with key equal to {key} (binary: {format(key, '08b')})")
    decrypted_chars = []
    # decrypt the text character by character
    for encrypted in cypher_text:
        decrypted = ord(encrypted) ^ key # convert character in cypher text into unicode and perform XOR function with key
        decrypted_chars.append(chr(decrypted)) # returns the character that represents the specified unicode(result) and put into list
    plain_text = ''.join(decrypted_chars) # make become a string
    return plain_text
# main execution
error = False
while not error:
    text = input("Enter message (or 'quit' to exit): ")
    # end execution if user want to
    if text.lower() == 'quit':
        break
    # generate random key
    key = gen_ran_key()
    # encrypt text
    encrypted_text = encrypt(text, key)
    print(f"Text encrypted to: {repr(encrypted_text)}")  # Using repr to show special chars
    # decrypt text
    dencrypted_text = decrypt(encrypted_text, key)
    print("text been dencrypt to", dencrypted_text)



