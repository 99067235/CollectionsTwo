import random

upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ['@', '#', '$', '%', '&', '_', '?']
password = []
def listToStringWithoutBrackets(password):
    return str(password).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')

def numberChoice():
    global l
    numberCheck = random.randint(4,7)
    for l in range(numberCheck):
        numberChoice = random.choice(numbers)
        password.append(numberChoice)
    chooseSpecialCharacters()

def chooseCapitalLetter():
    global i
    hoofdletterCheck = random.randint(2,6)
    for i in range(hoofdletterCheck):
        uppercaseChoice = random.choice(upperCaseLetters)
        password.append(uppercaseChoice)
    numberChoice()
    
def shuffle():
    random.shuffle(password)

def chooseSpecialCharacters():
    global d
    for d in range(3):
        specialCharacterChoice = random.choice(specialCharacters)
        password.append(specialCharacterChoice)
    
def chooseLowercaseLetter():
    global f
    for f in range(8):
        lowercaseLetterChoice = random.choice(lowerCaseLetters)
        password.append(lowercaseLetterChoice)
    chooseSpecialCharacters()

print(password)



chooseCapitalLetter()