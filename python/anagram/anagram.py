# This script should run in O(n) time per word
#   although it trades space for time.

def detect_anagrams(string, array):
    charArray1 = create_letter_array(string)
    anagramList = []
    
    for compareWord in array:
        if len(string) == len(compareWord) and \
           string.lower() != compareWord.lower():
            charArray2 = create_letter_array(compareWord)
            if compare_word_arrays(charArray1, charArray2):
                anagramList.append(compareWord)

    return anagramList                       


def create_letter_array(string):
    string = string.lower()
    charArray = [0] * 26
    for i in range(len(string)):
        pos = ord(string[i]) - ord('a')
        charArray[pos] += 1

    return charArray


def compare_word_arrays(charArray1, charArray2):
    is_anagram = True
    i = 0
    while i < 26 and is_anagram:
        if charArray1[i] == charArray2[i]:
            i += 1
        else:
            is_anagram = False

    return is_anagram




    
