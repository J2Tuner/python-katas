def abbreviate(string):
    string = string.replace('-', ' ')
    words = string.split(" ")
    acronym = ''
    for word in words:
        acronym += word[0].upper()

    return acronym
