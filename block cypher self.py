'''
Simple Block Cypher Demo Code (Symmetric)
Code below take user input to perform encryption and decryption for 2 round with XOR function and shift(substitution and permutation).
The main cypher key that used will be randomly generated for each input and the round key will generate based on the main cypher key.
'''
# import libraries
import random
import string
# declare needed variables
error = False
round_num = 2
block_size = 8 
block_len = 8 # each block can carry 8 bytes
# function to generate random main key
def gen_ran_main_key():
    ran_main_key = random.randint(1, 255)
    return ran_main_key
# function ensure block is fully filled
def check_text_len(text):
    num_space_need_fill = block_len - (len(text)%block_size)
    for i in range(num_space_need_fill):
        text += " "
    return text
# function remove space that filled
def remove_space(text):
    return text.rstrip()
# function to generate round key by using main key
def gen_round_keys(main_key, round_num):
    round_keys = []
    # create round key that equal to round needed
    for i in range(round_num):
        round_key = max(1, (main_key*11+i)%255) # prevent exceed 255 and 0
        round_keys.append(round_key)
    return round_keys
# function split text to blocks
def to_blocks(text, block_len):
    blocks = []
    for i in range(0, len(text), block_len):
        block = text[i:i+block_len]
        blocks.append(block)
    return blocks
# function join blocks to text
def join_blocks(blocks):
    join_text = ''.join(blocks)
    return join_text
# function to encrypt plain text
def encrypt(blocks, round_key):
    encrypted_blocks = []
    for block in blocks:
        encrypted_chars = []
        for char in block:
            encrypted = ord(char) ^ round_key # convert character in text into unicode and perform XOR function with key
            encrypted_chars.append(chr(encrypted)) # returns the character that represents the specified unicode(result) and put into list
        encrypted_chars = encrypted_chars[1:] + encrypted_chars[:1] # move 1st element from front to rear
        encrypted_block = ''.join(encrypted_chars) # make become a string
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks
# function to decrypt cypher text
def decrypt(blocks, round_key):
    decrypted_blocks = []
    for block in blocks:
        decrypted_chars = []
        for char in block:
            decrypted = ord(char) ^ round_key # convert character in text into unicode and perform XOR function with key
            decrypted_chars.append(chr(decrypted)) # returns the character that represents the specified unicode(result) and put into list
        decrypted_chars = decrypted_chars[-1:] + decrypted_chars[:-1]  # Combines the last element with elements from the beginning up to the second-to-last
        decrypted_block = ''.join(decrypted_chars) # make become a string
        decrypted_blocks.append(decrypted_block)
    return decrypted_blocks
# main execution
while not error:
    text = input("Enter message (or 'quit' to exit): ")
    # end execution if user want to
    if text.lower() == 'quit':
        break
    # check the input won't exit the limit
    if len(text) > block_len*block_size:
        print("The input is too large")
        continue
    # generate random main key and round key
    main_key = gen_ran_main_key()
    round_keys = gen_round_keys(main_key, round_num)
    # encrypt text
    fulfill_req_text = check_text_len(text)
    blocks = to_blocks(fulfill_req_text, block_len)
    for i in range(round_num):
        blocks = encrypt(blocks, round_keys[i])
    encrypted_blocks = blocks
    print(f"Text encrypted to: {repr(join_blocks(encrypted_blocks))}")  # Using repr to show special chars
    # decrypt text
    for i in range(round_num, 0, -1):
        encrypted_blocks = decrypt(encrypted_blocks, round_keys[i-1])
    decrypted_blocks = encrypted_blocks
    print("text been dencrypt to", remove_space(join_blocks(decrypted_blocks)))

