import numbers
import random
from tkinter.tix import Tree
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0
rondes = 0
finalscore = 0
gegooideStenen = {
    "dobbel1": 0,
    "dobbel2": 0,
    "dobbel3": 0,
    "dobbel4": 0,
    "dobbel5": 0,
}
topscore = {
    "enen": 0,
    "tweeën": 0,
    "drieën": 0,
    "vieren": 0,
    "vijven": 0,
    "zessen": 0,
}
bottomScore = {
    "ThreeOfAKind": 0,
    "FourOfAKind": 0,
    "FullHouse": 0,
    "SmallStraight": 0,
    "LargeStraight": 0,
    "Chance": 0,
    "Yahtzee": 0
}
unusedCombinations = ["Enen", "Tweën", "Drieën", "Vieren", "Vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]
<<<<<<< HEAD
totalThrown = gegooideStenen["dobbel1"] + gegooideStenen["dobbel2"] + gegooideStenen["dobbel4"] + gegooideStenen["dobbel5"]
=======
totaalGegooid = gegooideStenen["dobbel1"] + gegooideStenen["dobbel2"] + gegooideStenen["dobbel4"] + gegooideStenen["dobbel5"]
>>>>>>> 1d3c599c87ae927f38351b0b1994f95cc8cbca8d
amountOfDices = {"enen": 0, "tweeën": 0, "drieën": 0, "vieren": 0, "vijven": 0, "zessen": 0,}

def enenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
    global topscore
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
        topscore["enen"] += dobbelscore
        
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def tweeënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
        topscore["tweeën"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def drieënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
        topscore["drieën"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def vierenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
        topscore["vieren"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def vijvenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
        topscore["vijven"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def zessenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
        topscore["zessen"] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
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
            bottomScore["SmallStraight"] += 1
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

def largeStraight():
    global finalscore
    global largeStraightScore
    largeStraightScore = False
    if 1 in gegooideStenen.values() and 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values():
        print("Deze is 40 punten waard, wilt u deze gebruiken?")
        zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
        if zekerWeten == "Y":
            finalscore += 40
            unusedCombinations.remove("LargeStraight")
            bottomScore["LargeStraight"] += 1
        else:
            print("Oke, kies dan een andere.")
            besteden()
    else:
        print("U heeft helaas geen large straight gegooid, kies een andere.")
        besteden()
        
def fourOfAKind():
    global finalscore
    totalThrown = gegooideStenen["dobbel1"] + gegooideStenen["dobbel2"] + gegooideStenen["dobbel3"] + gegooideStenen["dobbel4"] + gegooideStenen["dobbel5"]
    for item in gegooideStenen.values():
        if item == 1:
            amountOfDices["enen"] += 1
        elif item == 2:
            amountOfDices["tweeën"] += 1
        elif item == 3:
            amountOfDices["drieën"] += 1
        elif item == 4:
            amountOfDices["vieren"] += 1
        elif item == 5:
            amountOfDices["vijven"] += 1
        elif item == 6:
            amountOfDices["zessen"] += 1
    
    if amountOfDices["enen"] >= 4:
        print("U hebt Four of a kind gegooid!")
    elif amountOfDices["tweeën"] >= 4:
        print("U hebt Four of a kind gegooid!")
    elif amountOfDices["drieën"] >= 4:
        print("U hebt Four of a kind gegooid!")
    elif amountOfDices["vieren"] >= 4:
        print("U hebt Four of a kind gegooid!")
    elif amountOfDices["vijven"] >= 4:
        print("U hebt Four of a kind gegooid!")
    elif amountOfDices["zessen"] >= 4:
        print("U hebt Four of a kind gegooid!")
    else:
        print("Helaas heeft u geen Four of a kind gegooid. Kies een andere.")
        besteden()
    print("Weet u zeker dat u deze wilt gebruiken voor", totalThrown, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("FourOfAKind")
        bottomScore["FourOfAKind"] += 1
        finalscore += totalThrown
    else:
        print("Oke, kies dan een andere.")
        besteden()

def fullHouse():
    global i
    ### checkt van welke dobbel er hoeveel zijn
    for item in gegooideStenen.values():
        if item == 1:
            amountOfDices["enen"] += 1
        elif item == 2:
            amountOfDices["tweeën"] += 1
        elif item == 3:
            amountOfDices["drieën"] += 1
        elif item == 4:
            amountOfDices["vieren"] += 1
        elif item == 5:
            amountOfDices["vijven"] += 1
        elif item == 6:
            amountOfDices["zessen"] += 1
    
    if amountOfDices["drieën"] == 3:
        for key, value in gegooideStenen.items():
            if value == 3:
                del gegooideStenen[key]
                break
    # checken of alle values in gegooidestenen gelijk zijn

        
        
        
        
        
        

def threeOfAKind():
<<<<<<< HEAD
    global totalThrown
    global finalscore
    totalThrown = gegooideStenen["dobbel1"] + gegooideStenen["dobbel2"] + gegooideStenen["dobbel3"] +  gegooideStenen["dobbel4"] + gegooideStenen["dobbel5"]
=======
    dobbelscore = 0
>>>>>>> 1d3c599c87ae927f38351b0b1994f95cc8cbca8d
    for item in gegooideStenen.values():
        if item == 1:
            amountOfDices["enen"] += 1
        elif item == 2:
            amountOfDices["tweeën"] += 1
        elif item == 3:
            amountOfDices["drieën"] += 1
        elif item == 4:
            amountOfDices["vieren"] += 1
        elif item == 5:
            amountOfDices["vijven"] += 1
        elif item == 6:
            amountOfDices["zessen"] += 1
    
    if amountOfDices["enen"] >= 3:
        print("U hebt Three of a kind gegooid!")
    elif amountOfDices["tweeën"] >= 3:
        print("U hebt Three of a kind gegooid!")
    elif amountOfDices["drieën"] >= 3:
        print("U hebt Three of a kind gegooid!")
    elif amountOfDices["vieren"] >= 3:
        print("U hebt Three of a kind gegooid!")
    elif amountOfDices["vijven"] >= 3:
        print("U hebt Three of a kind gegooid!")
    elif amountOfDices["zessen"] >= 3:
        print("U hebt Three of a kind gegooid!")
    else:
        print("Helaas heeft u geen Three of a kind gegooid. Kies een andere.")
        besteden()
<<<<<<< HEAD
    print("Weet u zeker dat u deze wilt gebruiken voor", totalThrown, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.remove("ThreeOfAKind")
        bottomScore["ThreeOfAKind"] += 1
        finalscore += totalThrown
    else:
        print("Oke, kies dan een andere.")
        besteden()

def chance():
    global finalscore
    print("Deze is", totalThrown, "punten waard, wilt u deze gebruiken?")
    zekerWeten = input("Typ hier uw antwoord Y/N: ")
    if zekerWeten == "Y":
        finalscore += totalThrown
        unusedCombinations.remove("Chance")
        bottomScore["Chance"] += 1
    else:
        print("Oke, kies dan een andere.")
        besteden()

def yahtzee():
    global finalscore
    if gegooideStenen["dobbel1"] == gegooideStenen["dobbel2"] == gegooideStenen["dobbel3"] == gegooideStenen["dobbel4"] == gegooideStenen["dobbel5"]:
        print("Gefeliciteerd! U heeft yahtzee gegooid!")
        weetZeker = input("Deze is 50 punten waard, wilt u deze gebruiken? Y/N ").upper()
        if weetZeker == "Y":
            unusedCombinations.remove("Yahtzee")
            bottomScore["Yahtzee"] += 1
            finalscore += 50
    else:
        print("Helaas heeft u nu geen yahtzee gegooid, probeer het opnieuw")
        besteden()

=======
>>>>>>> 1d3c599c87ae927f38351b0b1994f95cc8cbca8d
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
        elif besteed == 7 and "ThreeOfAKind" in unusedCombinations:
            threeOfAKind()
        elif besteed == 8 and "FourOfAKind" in unusedCombinations:
            fourOfAKind()
        elif besteed == 9 and "FullHouse" in unusedCombinations:
            fullHouse()
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
    except ValueError:
        print("vul a.u.b. een nummer in")
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
        gegooideStenen["dobbel1"] = dobbelKiezen()
        gegooideStenen["dobbel2"] = dobbelKiezen()
        gegooideStenen["dobbel3"] = dobbelKiezen()
        gegooideStenen["dobbel4"] = dobbelKiezen()
        gegooideStenen["dobbel5"] = dobbelKiezen()
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
    print(topscore)
    print(bottomScore)
    print("Huidige score:", finalscore)

    
print(finalscore)