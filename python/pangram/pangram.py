def is_pangram(string):
    string = string.lower()
    tokens = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(string)):
        tokens = tokens.replace(string[i], "")

    return len(tokens) == 0

