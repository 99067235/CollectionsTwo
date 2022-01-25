import random

upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ['@', '#', '$', '%', '&', '_', '?']
extraList = ['upperCaseLetters', 'lowerCaseLetters', 'numbers', 'specialCharacters' ]
password = []
kleineletters = 0
hoofdletters = 0
nummers = 0
specialeTekens = 0
aantalCharacters = 0
i = 0


def choose():
    global hoofdletters
    global kleineletters
    global i
    global aantalCharacters
    for l in range(3):
        choice = random.randint(1,3)
        if choice == 1 and kleineletters <8:
            lcChoice = random.choice(lowerCaseLetters)
            kleineletters += 1
            aantalCharacters += 1
            password.append(lcChoice)
        elif choice == 2 and hoofdletters <6:
            ucChoice = random.choice(upperCaseLetters)
            hoofdletters += 1
            aantalCharacters += 1
            password.append(ucChoice)
        elif choice == 3 and l > 1 and specialeTekens < 3:
            scChoice = random.choice(specialCharacters)
            password.append(scChoice)
            aantalCharacters += 1
    chooseLetters()

def chooseLetters():
    global hoofdletters
    global kleineletters
    global nummers
    global specialeTekens
    global aantalCharacters
    for i in range(21):
        choice2 = random.randint(1,4)
        if choice2 == 1 and hoofdletters < 6:
            ucChoice2 =  random.choice(upperCaseLetters)
            hoofdletters += 1
            aantalCharacters += 1
            password.append(ucChoice2)
        elif choice2 == 2 and kleineletters < 9:
            lcChoice2 = random.choice(lowerCaseLetters)
            listToStringWithoutBrackets(password)
            kleineletters += 1
            aantalCharacters += 1
            password.append(lcChoice2)
        elif choice2 == 3 and nummers < 4:
            numberchoice = random.choice(numbers)
            password.append(numberchoice)
            nummers += 1
            aantalCharacters += 1
        elif choice2 == 4 and i < 21 and specialeTekens < 3:
            specialCharacterChoice = random.choice(specialCharacters)
            password.append(specialCharacterChoice)
            specialeTekens += 1
            aantalCharacters += 1
        else:
            i = i - 1
    print(listToStringWithoutBrackets(password))

def listToStringWithoutBrackets(password):
    return str(password).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')


choose()