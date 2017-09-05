def hey(string):
    response = 'Whatever.'
    string = string.strip()
    
    if len(string) == 0: # String was empty or contained formatting info
        response = 'Fine. Be that way!'
    elif string.isupper(): # All uppercase
        response = 'Whoa, chill out!'
    elif string.endswith('?'): # String ends with a question mark
        response = 'Sure.'
    
    return response
        
