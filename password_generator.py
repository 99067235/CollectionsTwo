import random

upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ['@', '#', '$', '%', '&', '_', '?']
password = []
passwordSmallCharacters = []
LastSmallCharacters = []
totalOfCharacters = 0

def listToStringWithoutBrackets(password):
    return str(password).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')

def listToStringWithoutBrackets(passwordSmallCharacters):
    return str(passwordSmallCharacters).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')

def listToStringWithoutBrackets(LastSmallCharacters):
    return str(LastSmallCharacters).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')
    

def numberChoice():
    global totalOfCharacters
    numberCheck = random.randint(4,7)
    for l in range(numberCheck):
        numberChoice = random.choice(numbers)
        password.append(numberChoice)
        totalOfCharacters += 1
    chooseSpecialCharacters()


def chooseCapitalLetter():
    global totalOfCharacters
    hoofdletterCheck = random.randint(2,6)
    for i in range(hoofdletterCheck):
        uppercaseChoice = random.choice(upperCaseLetters)
        password.append(uppercaseChoice)
        totalOfCharacters += 1
    numberChoice()
    

def shuffle():
    random.shuffle(password)


def chooseSpecialCharacters():
    global totalOfCharacters
    for d in range(3):
        specialCharacterChoice = random.choice(specialCharacters)
        password.append(specialCharacterChoice)
        totalOfCharacters += 1
    chooseLowercaseLetter()
    
    
def chooseLowercaseLetter():
    global totalOfCharacters
    global passwordSmallCharacters
    global LastSmallCharacters
    amountOfLowercaseLetters = 24 - len(password)
    half = amountOfLowercaseLetters // 2
    for f in range(half):
        lowercaseLetterChoice = random.choice(lowerCaseLetters)
        passwordSmallCharacters.append(lowercaseLetterChoice)
        totalOfCharacters += 1
        random.shuffle(passwordSmallCharacters)
    for k in range(half):
        lowercaseLetterChoice = random.choice(lowerCaseLetters)
        LastSmallCharacters.append(lowercaseLetterChoice)
        totalOfCharacters += 1
        random.shuffle(LastSmallCharacters)
    print("password has been generated")
    print(listToStringWithoutBrackets(passwordSmallCharacters + password + LastSmallCharacters))
  

chooseCapitalLetter()