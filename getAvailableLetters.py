import string
def getAvailableltters(letterGuessed):
    out = ' '
    alphabet = string.ascii_lowercase
    for m in alphabet:
        if m in letterGuessed:
            continue
        else:
            out += m
            return out