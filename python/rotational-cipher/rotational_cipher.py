def rotate(string, key):
    cipherText = ''
    for char in string:
        if char.isalpha():
            charValue = ord(char)
            if char.islower():
                startIndex = ord('a')
            else:
                startIndex = ord('A')

            charValue -= startIndex - key

            if charValue > 25:
                charValue -= 26

            cipherText += chr(startIndex + charValue)
        else:
            cipherText += char
            
    return cipherText
