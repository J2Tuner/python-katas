import re

def decode(string):
    # Split input string into characters and character counts into list
    regex = re.compile(r'([A-Za-z ]|\d+)')
    decodeList = regex.findall(string)
    decodedString = ''
    runCount = 1

    # Create decoded string by iterating through decodeList
    i = 0
    while i < len(decodeList):
        if decodeList[i].isalpha() or decodeList[i].isspace() :
            j = 0
            while j < runCount:
                decodedString += decodeList[i]
                j += 1
            runCount = 1
        else:
            runCount = int(decodeList[i])
            
        i += 1
    return decodedString
    

def encode(string):
    i = 1
    runCount = 1
    encodedString = ''
    while i < len(string):
        if string[i] == string[i - 1] :
            runCount += 1
        else:
            # Add letter and run count to output string            
            encodedString = appendEncString(encodedString, runCount, string[i - 1])
            runCount = 1

        i += 1

    # Check for end of string case
    if len(string) > 0:
        encodedString = appendEncString(encodedString, runCount, string[-1])

    return encodedString


def appendEncString(string, runCount, char):
    if runCount > 1:
        string += str(runCount) + char
    else:
        string += char
        
    return string
