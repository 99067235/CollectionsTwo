import random
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0
rondes = 0
finalscore = 0
<<<<<<< HEAD
gegooideStenen = {
    "dobbel1": 0,
    "dobbel2": 0,
    "dobbel3": 0,
    "dobbel4": 0,
    "dobbel5": 0,
}
=======
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
score = {
    "enen": 0,
    "tweeën": 0,
    "drieën": 0,
    "vieren": 0,
    "vijven": 0,
    "zessen": 0,
}
<<<<<<< HEAD

=======
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
unusedCombinations = ["Enen", "Tweën", "Drieën", "Vieren", "Vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]


def enenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    global score
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 1:
        dobbelscore += 1
    if gegooideStenen["dobbel2"] == 1:
        dobbelscore += 1
    if gegooideStenen["dobbel3"] == 1:
        dobbelscore += 1
    if gegooideStenen["dobbel4"] == 1:
        dobbelscore += 1
    if gegooideStenen["dobbel5"] == 1:
        dobbelscore += 1
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Enen")
        finalscore += dobbelscore
        score["enen"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
=======
    if score == "enen" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 1:
            dobbelscore += 1
        if dobbel2 == 1:
            dobbelscore += 1
        if dobbel3 == 1:
            dobbelscore += 1
        if dobbel4 == 1:
            dobbelscore += 1
        if dobbel5 == 1:
            dobbelscore += 1
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Enen")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    rondes += 1

def tweeënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 2:
        dobbelscore += 2
    if gegooideStenen["dobbel2"] == 2:
        dobbelscore += 2
    if gegooideStenen["dobbel3"] == 2:
        dobbelscore += 2
    if gegooideStenen["dobbel4"] == 2:
        dobbelscore += 2
    if gegooideStenen["dobbel5"] == 2:
        dobbelscore += 2
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Tweën")
        finalscore += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
=======
    if score == "tweeën" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 2:
            dobbelscore += 2
        if dobbel2 == 2:
            dobbelscore += 2
        if dobbel3 == 2:
            dobbelscore += 2
        if dobbel4 == 2:
            dobbelscore += 2
        if dobbel5 == 2:
            dobbelscore += 2
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Tweën")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    rondes += 1

def drieënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 3:
        dobbelscore += 3
    if gegooideStenen["dobbel2"] == 3:
        dobbelscore += 3
    if gegooideStenen["dobbel3"] == 3:
        dobbelscore += 3
    if gegooideStenen["dobbel4"] == 3:
        dobbelscore += 3
    if gegooideStenen["dobbel5"] == 3:
        dobbelscore += 3
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Drieën")
        finalscore += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
=======
    if score == "drieën" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 3:
            dobbelscore += 3
        if dobbel2 == 3:
            dobbelscore += 3
        if dobbel3 == 3:
            dobbelscore += 3
        if dobbel4 == 3:
            dobbelscore += 3
        if dobbel5 == 3:
            dobbelscore += 3
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Drieën")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    rondes += 1

def vierenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 4:
        dobbelscore += 4
    if gegooideStenen["dobbel2"] == 4:
        dobbelscore += 4
    if gegooideStenen["dobbel3"] == 4:
        dobbelscore += 4
    if gegooideStenen["dobbel4"] == 4:
        dobbelscore += 4
    if gegooideStenen["dobbel5"] == 4:
        dobbelscore += 4
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Vieren")
        finalscore += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
=======
    if score == "vieren" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 4:
            dobbelscore += 4
        if dobbel2 == 4:
            dobbelscore += 4
        if dobbel3 == 4:
            dobbelscore += 4
        if dobbel4 == 4:
            dobbelscore += 4
        if dobbel5 == 4:
            dobbelscore += 4
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Vieren")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    rondes += 1

def vijvenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 5:
        dobbelscore += 5
    if gegooideStenen["dobbel2"] == 5:
        dobbelscore += 5
    if gegooideStenen["dobbel3"] == 5:
        dobbelscore += 5
    if gegooideStenen["dobbel4"] == 5:
        dobbelscore += 5
    if gegooideStenen["dobbel5"] == 5:
        dobbelscore += 5
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Vijven")
        finalscore += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
=======
    if score == "vijven" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 5:
            dobbelscore += 5
        if dobbel2 == 5:
            dobbelscore += 5
        if dobbel3 == 5:
            dobbelscore += 5
        if dobbel4 == 5:
            dobbelscore += 5
        if dobbel5 == 5:
            dobbelscore += 5
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Vijven")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    rondes += 1

def zessenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
<<<<<<< HEAD
    dobbelscore = 0
    if gegooideStenen["dobbel1"] == 6:
        dobbelscore += 6
    if gegooideStenen["dobbel2"] == 6:
        dobbelscore += 6
    if gegooideStenen["dobbel3"] == 6:
        dobbelscore += 6
    if gegooideStenen["dobbel4"] == 6:
        dobbelscore += 6
    if gegooideStenen["dobbel5"] == 6:
        dobbelscore += 6
    print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("Zessen")
        finalscore += dobbelscore
    else:
        print("Oke, kies dan een andere.")
=======
    if score == "vieren" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
        besteden()
    rondes += 1

def trueSmallStraight():
    global finalscore
    if smallStraightScore == True:
        print("Deze is 30 punten waard, wil je deze gebruiken?")
        zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
        if zekerWeten == "Y":
            finalscore += 30
            unusedCombinations.remove("SmallStraight")
        else:
            print("Oke, kies dan een andere.")
            besteden()

def smallStraight():
    global smallStraightScore
    global finalscore
    smallStraightScore = False
    if 1 in gegooideStenen.values() and 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values():
        smallStraightScore = True
        trueSmallStraight()
    elif 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values():
        smallStraightScore = True
        trueSmallStraight()
    elif 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values() and 6 in gegooideStenen.values():
        smallStraightScore = True
        trueSmallStraight()
    else:
        print("U heeft helaas geen small straight gegooid, kies een andere.")
        besteden()

def trueLargeStraight():
    global finalscore
    if largeStraightScore == True:
        print("Deze is 40 punten waard, wilt u deze gebruiken?")
        zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
        if zekerWeten == "Y":
<<<<<<< HEAD
            finalscore += 40
            unusedCombinations.remove("LargeStraight")
=======
            unusedCombinations.remove("Zessen")
            finalscore += dobbelscore
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
        else:
            print("Oke, kies dan een andere.")
            besteden()

def largeStraight():
    global finalscore
    global largeStraightScore
    largeStraightScore = False
    if 1 in gegooideStenen.values() and 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values():
        largeStraightScore = True
        trueLargeStraight()
    else:
        print("U heeft helaas geen large straight gegooid, kies een andere.")
        besteden()

def ThreeOfAKind():
    global finalscore
    dobbelscore = 0
    dobbelList = [dobbel1, dobbel2, dobbel3, dobbel4, dobbel5,]
    ones = dobbelList.count(1)
    twos = dobbelList.count(2)
    threes = dobbelList.count(3)
    fours = dobbelList.count(4)
    fives = dobbelList.count(5)
    sixes = dobbelList.count(6)
    
    if ones >= 3:
        dobbelscore += ones
    elif twos >= 3:
        twos = twos * 2
        dobbelscore += twos
    elif threes >= 3:
        threes = threes * 3
        dobbelscore += threes
    elif fours >= 3:
        fours = fours * 4
        dobbelscore += fours
    elif fives >= 3:
        fives = fives * 5
        dobbelscore += fives
    elif sixes >= 3:
        sixes = sixes * 6
        dobbelscore += sixes
    
    print("Dit is",dobbelscore,"punten waard, wil je het hiervoor gebruiken?")
    zekerWeten = input("Vul hier uw antwoord in (Y/N): ").upper()
    if zekerWeten  == "Y":
        unusedCombinations.remove("ThreeOfAKind")
        finalscore += dobbelscore

        

    

def besteden():
    print("Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)","Chance(12)","Yahtzee(13)")
    print("Waar wil je je punten aan uitgeven? ")
    try:
        besteed = int(input("typ hier een nummer: "))
        if besteed == 1 and "Enen" in unusedCombinations:
            enenBerekenen()
        elif besteed == 2 and "Tweën" in unusedCombinations:
            tweeënBerekenen()
        elif besteed == 3 and "Drieën" in unusedCombinations:
            drieënBerekenen()
        elif besteed == 4 and "Vieren" in unusedCombinations:
            vierenBerekenen()
        elif besteed == 5 and "Vijven" in unusedCombinations:
            vijvenBerekenen()
        elif besteed == 6 and "Zessen" in unusedCombinations:
            zessenBerekenen()
<<<<<<< HEAD
        elif besteed == 10 and "SmallStraight" in unusedCombinations:
            smallStraight()
        elif besteed == 11 and "LargeStraight" in unusedCombinations:
            largeStraight()
        elif besteed == 12 and "Chance" in unusedCombinations:
            chance()
        elif besteed == 13 and "Yahtzee" in unusedCombinations:
            yahtzee()
        else:
            print("Deze is al een keer gebruikt, probeer een andere.")
            besteden()
=======
        elif besteed == 7:
            ThreeOfAKind()
>>>>>>> 0760ed6da61a15459b2f1fda68179f0687ee319b
    except ValueError:
        print("vul a.u.b. een nummer in")
        besteden()

def chance():
    chance = dobbel1 + dobbel2 + dobbel3 + dobbel4 + dobbel5
    print(chance)

def yahtzee():
    global dobbelscore
    dobbellist = [dobbel1, dobbel2, dobbel3, dobbel4, dobbel5]
    check = all(element == dobbellist[0] for element in dobbellist)
    if check == True:
        print("Gefeliciteerd! U heeft yahtzee gegooid!")
        dobbelscore += 50
    else:
        print("Helaas heeft u nu geen yahtzee gegooid, probeer het opnieuw")
        besteden()

def keep():
    global houden1
    global houden2
    global houden3
    global houden4
    global houden5

    houden1 = input("Wil je dobbelsteen 1 houden? Y/N ").upper()
    houden2 = input("Wil je dobbelsteen 2 houden? Y/N ").upper()
    houden3 = input("Wil je dobbelsteen 3 houden? Y/N ").upper()
    houden4 = input("Wil je dobbelsteen 4 houden? Y/N ").upper()
    houden5 = input("Wil je dobbelsteen 5 houden? Y/N ").upper()

def dobbelKiezen():
    getalkiezen = random.randint(1,6)
    return getalkiezen

def gooien():
    global dobbel1
    global dobbel2
    global dobbel3
    global dobbel4
    global dobbel5
    global i
    
    input("Druk op enter om de dobbelstenen te gooien ")
    if i == 0:
        gegooideStenen["dobbel1"] = 1
        gegooideStenen["dobbel2"] = 2
        gegooideStenen["dobbel3"] = 3
        gegooideStenen["dobbel4"] = 4
        gegooideStenen["dobbel5"] = 5
    for key, value in gegooideStenen.items():
        print(key, ':', value)
    
    keep()

    if houden1 == "Y":
        pass
    else:
        gegooideStenen["dobbel1"] = dobbelKiezen()
    if houden2 == "Y":
        pass
    else:
        gegooideStenen["dobbel2"] = dobbelKiezen()
    if houden3 == "Y":
        pass
    else:
        gegooideStenen["dobbel3"] = dobbelKiezen()
    if houden4 == "Y":
        pass
    else:
        gegooideStenen["dobbel4"] = dobbelKiezen()
    if houden5 == "Y":
        pass
    else:
        gegooideStenen["dobbel5"] = dobbelKiezen()


while rondes < 4:
    for i in range(3):
        gooien()
    besteden()
    
print(finalscore)