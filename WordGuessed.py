def isWordGuessed(secretWord,letterGuessed):
    for m in secretWord:
        if m in letterGuessed:
            return True
        else:
            return False