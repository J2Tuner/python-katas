def detect_anagrams(string, array):
    string = string.lower()
    anagram = sorted(string)
    candidates = (c for c in array if c.lower() != string)
    return [c for c in candidates if sorted(c.lower()) == anagram]
