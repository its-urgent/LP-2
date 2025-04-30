import math

def get_ordered_key_indices(key):
    return [i for i, _ in sorted(enumerate(key), key=lambda x: x[1])]

def encrypt_columnar(plain_text, key):
    key_length = len(key)
    ordered_indices = get_ordered_key_indices(key)

    # Padding with 'X' to fill the matrix
    rows = math.ceil(len(plain_text) / key_length)
    padded_text = plain_text.ljust(rows * key_length, 'X')

    # Create the matrix
    matrix = [padded_text[i:i+key_length] for i in range(0, len(padded_text), key_length)]

    # Read columns in the order of the sorted key
    cipher_text = ''
    for index in ordered_indices:
        for row in matrix:
            cipher_text += row[index]

    return cipher_text

def decrypt_columnar(cipher_text, key):
    key_length = len(key)
    ordered_indices = get_ordered_key_indices(key)
    rows = int(len(cipher_text) / key_length)

    # Create an empty matrix
    matrix = [''] * key_length
    start = 0

    # Fill the columns in the correct order
    for index in ordered_indices:
        matrix[index] = cipher_text[start:start+rows]
        start += rows

    # Read the matrix row-wise
    plain_text = ''
    for i in range(rows):
        for j in range(key_length):
            plain_text += matrix[j][i]

    return plain_text.rstrip('X')  # Remove padding

# Example
plaintext = "WEAREDISCOVEREDFLEEATONCE"
key = "ZEBRAS"

encrypted = encrypt_columnar(plaintext, key)
print("Encrypted:", encrypted)

decrypted = decrypt_columnar(encrypted, key)
print("Decrypted:", decrypted)
