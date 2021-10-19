# Alisha Agrawal (aa3se) Shelby Peak (sap2ej)


def encrypt_shift(plain_text, key):
    """
    index and search alphabet for character in plain_text
    add key to index
    :param plain_text: text to be encrypted
    :param key: shift size
    :return: encrypted plain_text
    """
    cipher_text = ''  # accumulator pattern: start with no encrypted test
    for i in range(0, len(plain_text)):
        alp = "abcdefghijklmnopqrstuvwxyz"
        character = plain_text[i]
        index = alp.find(character)
        if index == -1:
            alp = alp.upper()
            index = alp.find(character)
        new = index + key
        cipher_text += alp[new % 26]
    return cipher_text


def decrypt_shift(plain_text, key):
    """
    calls encrypted_shift function
    reverses to return normal plain_text
    :param plain_text: text to decrypted
    :param key: shift size
    :return: decrypted text
    """
    return encrypt_shift(plain_text, -key)


to_encrypt = encrypt_shift("secret", 9)
print(encrypt_shift("secret", 9))
print(decrypt_shift(to_encrypt, 9))
