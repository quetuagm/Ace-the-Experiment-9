def getGuessedWord(secretWord,letterGuessed):
    word = " "
    while len(secretWord) > 0:
        m = " "
    missed = 0
    for letterGuessed in secretWord:
        if letterGuessed in letterGuessed:
            m =m + letterGuessed
        else:
            m = m + "_" + " "
            missed +=1
            return word