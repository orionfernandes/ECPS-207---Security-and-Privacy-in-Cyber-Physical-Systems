def _pad_key(plaintext, key):     #creating pad key
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key

def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):      #encypting and decrypting based on mode
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'

        old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)
        key_char_position = ord(key_char.lower()) - ord('a')

        if mode == 'encrypt':
            new_char_position = (old_char_position + key_char_position) % 26
        else:
            new_char_position = (old_char_position - key_char_position + 26) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintext_char

def encrypt(plaintext, key):          #encryption function
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)
    for plaintext_char, key_char in zip(plaintext, padded_key):
        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)
    return ciphertext

def decrypt(ciphertext, key):         #decryption function
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)
    for ciphertext_char, key_char in zip(ciphertext, padded_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode='decrypt')
    return plaintext

file_name= input("Enter file name: ")
plaintext = input('Enter a message: ')
key = input('Enter a key: ')


fh = open(file_name, 'w') #fh = file handler
ciphertext = encrypt(plaintext, key)

fh.write(f'Plaintext: {plaintext}\n')
fh.write(f'Ciphertext: {ciphertext}')

fh.close()

