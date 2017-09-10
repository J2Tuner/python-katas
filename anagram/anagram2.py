def detect_anagrams(string, array):
    return [a for a in array 
            if a.lower()!=string.lower() 
            and sorted(a.lower())==sorted(string.lower())]
