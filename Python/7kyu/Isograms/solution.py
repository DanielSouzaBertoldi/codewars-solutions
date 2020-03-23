# Calculates the ocurrence of every letter of the word.
# If it can't find more than one ocurrence for every letter,
# then it's an isogram.

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

# That was my first try at this challenge. Then ocurred to me
# you could use the set() function and just compare the
# lengths, like so:

def is_isogram(string):
    return len(string) == len(set(string.lower()))