def is_isogram(string):
    # Format Input String
    string = string.lower()
    ok_tokens = "abcdefghijklmnopqrstuvwxyz"

    # Remove non-alphabetic characters from string
    for c in string:
        if c not in ok_tokens:
            string = string.replace(c, "")
        
    # Check if string is an isogram
    for i in range(len(string)):        
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False

    return True
