import re

def word_count(string):
    # Format string
    string = string.lower()
    string = re.findall(r'\d+|[A-Za-z]+', string)

    words = {}
    
    for word in string:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words


    
        
