def isWordGuessed(secretWord,letterGuessed):
    for m in secretWord:
        if m in letterGuessed:
            return True
        else:
            return False
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

def hangaroo(secretWord):
    print("Welcome to the Game! You only have maximum of 10 tries to finish the Game!")
    print()
secretWord={"molave"} 
validletters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
turns=10
letterGuessed=input("Enter a letter: ")
letterLC= letterGuessed.lower()
while len(secretWord) > 0:
    missed=0
    if secretWord!= getGuessedWord(secretWord, letterGuessed):
        if letterLC not in secretWord:
            print("Try again")
        elif letterLC not in secretWord:
            print("Try again")
        else:
            letterGuessed.append(letterLC)
            print("Correct")
    else:
        print("Congrats! You guessed it!")
        print(secretWord)
        break
    