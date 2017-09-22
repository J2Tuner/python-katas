def say(n):
    if n < 0 or n >= 1e12:
        raise AttributeError
    
    splitNum = split_string(str(int(n)))
    result = generate_text(splitNum)
    result.reverse()
    return " ".join(result)


def split_string(string):
    trimmedStr = string
    digitGroups = []
    i = 0
    
    while i < len(trimmedStr):
        strLen = len(trimmedStr)
        if strLen % 3 > 0:
            digitGroups.append(int(trimmedStr[0:strLen % 3]))
            trimmedStr = trimmedStr[strLen % 3:]
        else:
            digitGroups.append(int(trimmedStr[0: 3]))
            trimmedStr = trimmedStr[3:]

    return digitGroups


def generate_text(numberList):
    remainingNumbers = numberList.copy()
    digitGroupNumber = 0
    numberText = []
    
    while len(remainingNumbers) > 0:
        workingDigits = remainingNumbers.pop()
        workingReference = workingDigits
        digitGroupNumber += 1
        
        # Add text for orders of magnitude
        if digitGroupNumber > 1 and workingReference > 0:
            # Send group number to function to get magnitude
            numberText.append(generate_magnitudes(digitGroupNumber))
      
        # Add text for ones and tens digits
        if len(numberList) == 1 and workingDigits == 0:
            # Return zero if the original number was zero
            numberText.append(generate_ones_through_teens(workingDigits % 100))
        elif workingDigits % 100 < 20 and workingDigits % 100 > 0:
            # Return text for one through nineteen
            numberText.append(generate_ones_through_teens(workingDigits % 100))
        elif workingDigits % 100 != 0:
            # Return text for ones digit, then tens digit
            if workingDigits % 10 != 0:
                numberText.append(generate_ones_through_teens(workingDigits % 10))
                workingDigits -= workingDigits % 10

            tensValue = generate_tens(workingDigits % 100)
            
            # Add hyphen between tens and ones digit if necessary
            if workingReference % 100 > 20 and workingReference % 10 > 0:
                numberText[-1] = tensValue + '-' + numberText[-1]
            else:    
                numberText.append(tensValue)

        workingDigits -= workingDigits % 100    

        # Add text for 'and'
        if (workingReference > 100 and workingReference % 1000 > 0) or \
           (workingReference > 0 and digitGroupNumber == 1 and \
            len(numberList) > 1):
            numberText.append('and')
            
        # Add text for hundreds digit
        if workingDigits % 1000 > 0:
            numberText.append('hundred')
            # Get hundreds value, then get text value
            workingDigits //= 100
            numberText.append(generate_ones_through_teens(workingDigits))

    return numberText
                                  

def generate_ones_through_teens(digits):
    onesWords = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
                 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
                 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
                 14:'fourteen', 15:'fifteen', 16:'sixteen',
                 17:'seventeen', 18:'eighteen', 19:'nineteen'}

    return onesWords[digits]
                                  

def generate_tens(digit):
    tensWords = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
                 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

    return tensWords[digit]

def generate_magnitudes(groupNumber):
    magnitudes = {2:'thousand', 3:'million', 4:'billion', 5:'trillion'}

    return magnitudes[groupNumber]
