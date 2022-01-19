import random
i = 0
upperCaseLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowerCaseLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ['@', '#', '$', '%', '&', '_', '?']
password = []
kleineletters = 0
hoofdletters = 0
nummers = 0
specialeTekens = 0

def choose():
    global hoofdletters
    global kleineletters
    global i
    while i < 24:
        choose = random.randint(1,2)
        if choose == 1:
            choose1 =  random.choice(upperCaseLetters)
            hoofdletters += 1
            password.append(choose1)
            i = i + 1
        
        else:
            choose2 = random.choice(lowerCaseLetters)
            listToStringWithoutBrackets(password)
            kleineletters += 1
            password.append(choose2)
            i = i + 1
    print(listToStringWithoutBrackets(password))
    
def listToStringWithoutBrackets(password):
    return str(password).replace('[','').replace(']','').replace("'", '').replace(",", '').replace(' ', '')


choose()