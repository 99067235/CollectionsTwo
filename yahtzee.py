import random
import time
valueCheck1 = 0
valueCheck2 = 0 
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
allCombinations = ["Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)","Chance(12)","Yahtzee(13)", "Een combinatie wegstrepen(14)"]
unusedCombinations = ["Enen", "Tweën", "Drieën", "Vieren", "Vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]
amountOfDices = {"enen": 0, "tweeën": 0, "drieën": 0, "vieren": 0, "vijven": 0, "zessen": 0}
totalThrown = sum(gegooideStenen.values())


def scorekaart():
    print("bezig met berekenen van huidige score...")
    time.sleep(1)
    print("------------------------------------------------------[scorekaart]------------------------------------------------------")
    print(topscore)
    print(bottomScore)
    print("------------------------------------------------------------------------------------------------------------------------")

def trueSmallStraight():
    global finalscore
    if smallStraightScore == True:
        print("Deze is 30 punten waard, wil je deze gebruiken?")
        zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
        if zekerWeten == "Y":
            finalscore += 30
            allCombinations.remove("SmallStraight(10)")
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

def trueLargeStraight():
    global finalscore
    print("Deze is 40 punten waard, wilt u deze gebruiken?")
    zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
    if zekerWeten == "Y":
        finalscore += 40
        allCombinations.remove("LargeStraight(11)")
        unusedCombinations.remove("LargeStraight")
        bottomScore["LargeStraight"] += 1
    else:
        print("Oke, kies dan een andere.")
        besteden()

def largeStraight():
    global finalscore
    global largeStraightScore
    largeStraightScore = False
    if 1 in gegooideStenen.values() and 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values():
        trueLargeStraight()
    elif 2 in gegooideStenen.values() and 3 in gegooideStenen.values() and 4 in gegooideStenen.values() and 5 in gegooideStenen.values() and 6 in gegooideStenen.values():
        trueLargeStraight()
    else:
        print("U heeft helaas geen large straight gegooid, kies een andere.")
        besteden()

def ThreeOrFourOfAKind(besteed, chosenCombination):
    global finalscore
    totalThrown = sum(gegooideStenen.values())
    if besteed == 7:
        amount = 3
    elif besteed == 8:
        amount = 4
    else:
        print("kies een andere")

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
    
    if amountOfDices["enen"] >= amount:
        pass
    elif amountOfDices["tweeën"] >= amount:
        pass
    elif amountOfDices["drieën"] >= amount:
        pass
    elif amountOfDices["vieren"] >= amount:
        pass
    elif amountOfDices["vijven"] >= amount:
        pass
    elif amountOfDices["zessen"] >= amount:
        pass
    else:
        print("Helaas heeft u geen Four of a kind gegooid. Kies een andere.")
        besteden()
    print("Weet u zeker dat u deze wilt gebruiken voor", totalThrown, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        allCombinations.pop(besteed - 1)
        unusedCombinations.pop(besteed - 1)
        bottomScore[chosenCombination] += totalThrown
        finalscore += totalThrown
    else:
        print("Oke, kies dan een andere.")
        besteden()

def fullHouseCheck(valueNumber):
    for i in range(3):
        for key, value in gegooideStenen.items():
            if value == valueNumber:
                del gegooideStenen[key]
                break
            else:
                pass

def fullHouse():
    global i, finalscore, gegooideStenen
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
    
    if amountOfDices["enen"] == 3:
        fullHouseCheck(1)
    elif amountOfDices["tweeën"] == 3:
        fullHouseCheck(2)
    elif amountOfDices["drieën"] == 3:
        fullHouseCheck(3)
    elif amountOfDices["vieren"] == 3:
        fullHouseCheck(4)
    elif amountOfDices["vijven"] == 3:
        fullHouseCheck(5)
    elif amountOfDices["zessen"] == 3:
        fullHouseCheck(6)

    for i in range(2):
        for key, value in gegooideStenen.items():
            if i == 0:
                valueCheck1 = value
                i = i + 1
            elif i == 1:
                valueCheck2 = value
        
    if valueCheck1 == valueCheck2:
        print("Deze is 25 punten waard, wilt u deze gebruiken?")
        zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
        if zekerWeten == "Y":
            finalscore += 25
            bottomScore["FullHouse"] += 1
            unusedCombinations.remove("FullHouse")
            allCombinations.remove("FullHouse(9)")
        else:
            print("Oke, kies dan een andere.")
            gegooideStenen = {
            "dobbel1": 0,
            "dobbel2": 0,
            "dobbel3": 0,
            "dobbel4": 0,
            "dobbel5": 0,
            }
            gegooideStenen = dict.fromkeys(gegooideStenen, 0)
            besteden()
        
    else:
        print("U hebt helaas geen Fullhouse gegooid, probeer het opnieuw.")
        besteden()
    gegooideStenen = {
    "dobbel1": 0,
    "dobbel2": 0,
    "dobbel3": 0,
    "dobbel4": 0,
    "dobbel5": 0,
}


def chance():
    global finalscore
    totalThrown = sum(gegooideStenen.values())
    print("Deze is", totalThrown, "punten waard, wilt u deze gebruiken?")
    zekerWeten = input("Typ hier uw antwoord Y/N: ").upper()
    if zekerWeten == "Y":
        finalscore += totalThrown
        allCombinations.remove("Chance(12)")
        unusedCombinations.remove("Chance")
        bottomScore["Chance"] += 1
    else:
        print("Oke, kies dan een andere.")
        besteden()

def yahtzee():
    global finalscore
    if gegooideStenen["dobbel1"] == gegooideStenen["dobbel2"] == gegooideStenen["dobbel3"] == gegooideStenen["dobbel4"] == gegooideStenen["dobbel5"]:
        print("U hebt yahtzee gegooid!")
        weetZeker = input("Deze is 50 punten waard, wilt u deze gebruiken? Y/N ").upper()
        if weetZeker == "Y":
            allCombinations.remove("Yahtzee(13)")
            unusedCombinations.remove("Yahtzee")
            bottomScore["Yahtzee"] += 1
            finalscore += 50
    else:
        print("Helaas heeft u nu geen yahtzee gegooid, probeer het opnieuw")
        besteden()

def zekerWegstrepen():
    zekerWeten = input("Weet je zeker dat je deze wilt wegstrepen?").upper()
    if zekerWeten == "Y":
        pass
    else:
        print("Oke probeer het opnieuw.")
        besteden()

def wegstrepen():
    global antwoord
    print("Welke combinatie wil je wegstrepen?")
    antwoord = int(input("Vul hier een nummer in: "))
    if antwoord == 1:
        zekerWegstrepen()
        allCombinations.remove("Enen(1))")
        unusedCombinations.remove("Enen")
    elif antwoord == 2:
        zekerWegstrepen()
        allCombinations.remove("Tweën(2)")
        unusedCombinations.remove("Tweën")
    elif antwoord == 3:
        zekerWegstrepen()
        allCombinations.remove("Drieën(3)")
        unusedCombinations.remove("Drieën")
    elif antwoord == 4:
        zekerWegstrepen()
        allCombinations.remove("Vieren(4)")
        unusedCombinations.remove("Vieren")
    elif antwoord == 5:
        zekerWegstrepen()
        allCombinations.remove("vijven(5)")
        unusedCombinations.remove("Vijven")
    elif antwoord == 6:
        zekerWegstrepen()
        allCombinations.remove("Zessen(6)")
        unusedCombinations.remove("Zessen")
    elif antwoord == 7:
        zekerWegstrepen()
        allCombinations.remove("ThreeOfAKind(7)")
        unusedCombinations.remove("ThreeOfAKind")
    elif antwoord == 8:
        zekerWegstrepen()
        allCombinations.remove("FourOfAKind(8)")
        unusedCombinations.remove("FourOfAKind")
    elif antwoord == 9:
        zekerWegstrepen()
        allCombinations.remove("FullHouse(9)")
        unusedCombinations.remove("FullHouse")
    elif antwoord == 10:
        zekerWegstrepen()
        allCombinations.remove("SmallStraight(10)")
        unusedCombinations.remove("SmallStraight")
    elif antwoord == 11:
        zekerWegstrepen()
        allCombinations.remove("LargeStraight(11)")
        unusedCombinations.remove("LargeStraight")
    elif antwoord == 12:
        zekerWegstrepen()
        allCombinations.remove("Chance(12)")
        unusedCombinations.remove("Chance")
    elif antwoord == 13:
        zekerWegstrepen()
        allCombinations.remove("Yahtzee(13)")
        unusedCombinations.remove("Yahtzee")
    else:
        print("Kies een nummer uit de lijst.")
        wegstrepen()

def bovenHelft(besteed, besteedString):
    global rondes,finalscore
    dobbelscore = 0
    for value in gegooideStenen:
        if besteed == gegooideStenen[value]:
            dobbelscore += 1
        else:
            pass
    print("Weet u zeker dat u deze wilt gebruiken voor", besteed * dobbelscore, "punten? ")
    zekerWeten = input("Typ hier uw antwoord: ").upper()
    if zekerWeten == "Y":
        unusedCombinations.pop(besteed - 1)
        allCombinations.pop(besteed - 1)
        finalscore += dobbelscore
        topscore[besteedString] += dobbelscore
    else:
        print("Oke, kies dan een andere.")
        besteden()
    rondes += 1

def besteden():
    print(allCombinations)
    print("Waar wil je je punten aan uitgeven? ")
    try:
        besteed = int(input("typ hier een nummer: "))
        if besteed == 1 and "Enen" in unusedCombinations:
            bovenHelft(besteed, "enen")
        elif besteed == 2 and "Tweën" in unusedCombinations:
            bovenHelft(besteed, "tweeën")
        elif besteed == 3 and "Drieën" in unusedCombinations:
            bovenHelft(besteed, "drieën")
        elif besteed == 4 and "Vieren" in unusedCombinations:
            bovenHelft(besteed, "vieren")
        elif besteed == 5 and "Vijven" in unusedCombinations:
            bovenHelft(besteed, "vijven")
        elif besteed == 6 and "Zessen" in unusedCombinations:
            bovenHelft(besteed, "zessen")
        elif besteed == 7 and "ThreeOfAKind" in unusedCombinations:
            ThreeOrFourOfAKind(besteed, "ThreeOfAKind")
        elif besteed == 8 and "FourOfAKind" in unusedCombinations:
            ThreeOrFourOfAKind(besteed, "FourOfAKind")
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
        elif besteed == 14:
            wegstrepen()
        else:
            print("Deze is al een keer gebruikt, probeer een andere.")
            besteden()
    except ValueError:
        print("vul a.u.b. een nummer in")
        besteden()

def keep():
    global houden1, houden2, houden3, houden4, houden5
    houden1 = input("Wil je dobbelsteen 1 houden? Y/N ").upper()
    houden2 = input("Wil je dobbelsteen 2 houden? Y/N ").upper()
    houden3 = input("Wil je dobbelsteen 3 houden? Y/N ").upper()
    houden4 = input("Wil je dobbelsteen 4 houden? Y/N ").upper()
    houden5 = input("Wil je dobbelsteen 5 houden? Y/N ").upper()

def dobbelKiezen():
    getalkiezen = random.randint(1,6)
    return getalkiezen

def gooien():
    global i
    
    input("Druk op enter om de dobbelstenen te gooien ")
    if i == 0:
        gegooideStenen["dobbel1"] = 4
        gegooideStenen["dobbel2"] = 4
        gegooideStenen["dobbel3"] = 4
        gegooideStenen["dobbel4"] = 4
        gegooideStenen["dobbel5"] = 3
    else:
        pass

    for key, value in gegooideStenen.items():
        print(key, ':', value)
    
    if i < 2:
        keep()
    else:
        pass
    
    if i < 2:
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

for g in range(13):
    print("------------------------")
    print("Huidige ronde: ", g + 1)
    print("------------------------")
    for i in range(3):
        gooien()
    besteden()

    scorekaart()


print("Dat waren alle rondes, uw eindscore wordt nu berekent.")
time.sleep(3)
print("UW eindscore is:", finalscore)