def say(n):
    lowNumWords = ['zero', 'one', 'two', 'three', 'four',
                   'five', 'six', 'seven', 'eight', 'nine',
                   'ten', 'eleven', 'twelve', 'thirteen',
                   'fourteen', 'fifteen', 'sixteen', 'seventeen',
                   'eighteen', 'nineteen', 'twenty']

    tensWords = [(30, 'thirty'), (40, 'forty'), (50, 'fifty'),
                 (60, 'sixty'), (70, 'seventy'), (80, 'eighty'),
                 (90, 'ninety'), (100, 'hundred'), (1000, 'thousand')]
    
    magnitudes = ['million', 'billion', 'trillion']

    split_num = [x for x in str(n)]

def split_string(string):
    trimmedString = string
    digitGroups = []
    i = len(string) - 1
    
    while len(trimmedString) > 0:
        stringLength = len(trimmedString)
        print(trimmedString)
        print(trimmedString[stringLength - 1: stringLength - 4 : -1])
        digitGroups.append(trimmedString[stringLength - 1: stringLength - 4 : -1])
        trimmedString = trimmedString[:stringLength - 3]

    return digitGroups

m = '123456789'
