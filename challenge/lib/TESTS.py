def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
  
    return print("".join(ciphertext_chars))


def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f"CIPHER {cipher}")
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)
    print(f"PLAINTEXTCHARS {plaintext_chars}")
    return print("".join(plaintext_chars))


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    cipher_with_duplicates = list(key) + alphabet
    print(f"ALPHABET {alphabet}")
    print(f"DUPLICATE {cipher_with_duplicates}")
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')
encode('mechamoigoresouatleticano', 'cesarcipher')
decode('PBAHDPRFLREBCRUDTOBTFADQR', 'cesarcipher')