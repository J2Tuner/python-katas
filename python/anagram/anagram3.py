def detect_anagrams(string, array):
    out = list()
    for word in array:
        if(are2Anagrams(string,word)):
            out.append(word)
    return out

def are2Anagrams(a,b):

    if(len(a)!=len(b)):
        return False

    a = a.lower()
    b = b.lower()

    if a == b :
        return False

    uniqueSet = set(a)

    for ch in uniqueSet:
        if(a.count(ch) != b.count(ch)):
            return  False

    return True
