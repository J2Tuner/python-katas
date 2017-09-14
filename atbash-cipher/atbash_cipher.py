import itertools

def encode(string, wordLength = 5):
    # Format input string
    string = string.replace(" ", "").lower()
    cipherText = ''

    # Replace characters with encoded values
    for char in string:
        if char.isalpha():
            cipherText += chr(ord('z') - (ord(char) - ord('a')))
        elif char.isnumeric():
            cipherText += char

    # Add spaces between words at interval specified by wordLength
    cipherText = " ".join([''.join(x) for x in itertools.zip_longest( \
                          *[iter(cipherText)]*wordLength, fillvalue='')])

    return cipherText


def decode(string):
    decryptedText = ''
    for char in string:
        if char.isalpha():
            decryptedText += chr(ord('a') + (ord('z') - ord(char)))
        elif char.isnumeric():
            decryptedText += char

    return decryptedText
