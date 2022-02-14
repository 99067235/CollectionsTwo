import random
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0
rondes = 0
finalscore = 0
score = {
    "enen": 0,
    "tweeën": 0,
    "drieën": 0,
    "vieren": 0,
    "vijven": 0,
    "zessen": 0,
}
unusedCombinations = ["Enen", "Tweën", "Drieën", "Vieren", "Vijven", "Zessen", "ThreeOfAKind", "FourOfAKind","FullHouse","SmallStraight","LargeStraight","Chance","Yahtzee"]


def enenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
    rondes += 1


def tweeënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
    rondes += 1


def drieënBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
    rondes += 1
def vierenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
    rondes += 1


def vijvenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
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
    rondes += 1


def zessenBerekenen():
    global rondes
    global dobbelscore
    global finalscore
    if score == "vieren" > 0:
        print("Deze is al een keer gebruikt, kies aub een andere")
        besteden()
    else:
        dobbelscore = 0
        if dobbel1 == 6:
            dobbelscore += 6
        if dobbel2 == 6:
            dobbelscore += 6
        if dobbel3 == 6:
            dobbelscore += 6
        if dobbel4 == 6:
            dobbelscore += 6
        if dobbel5 == 6:
            dobbelscore += 6
        print("Weet u zeker dat u deze wilt gebruiken voor", dobbelscore, "punten? ")
        zekerWeten = input("Typ hier uw antwoord: ").upper()
        if zekerWeten == "Y":
            unusedCombinations.remove("Zessen")
            finalscore += dobbelscore
        else:
            print("Oke, kies dan een andere.")
            besteden()
    rondes += 1


def besteden():
    print("Enen(1)", "Tweën(2)", "Drieën(3)", "Vieren(4)", "vijven(5)", "Zessen(6)", "ThreeOfAKind(7)", "FourOfAKind(8)","FullHouse(9)","SmallStraight(10)","LargeStraight(11)","Chance(12)","Yahtzee(13)")
    print("Waar wil je je punten aan uitgeven? ")
    try:
        besteed = int(input("typ hier een nummer: "))
        if besteed == 1:
            enenBerekenen()
        elif besteed == 2:
            tweeënBerekenen()
        elif besteed == 3:
            drieënBerekenen()
        elif besteed == 4:
            vierenBerekenen()
        elif besteed == 5:
            vijvenBerekenen()
        elif besteed == 6:
            zessenBerekenen()
        elif besteed == 12:
            chance()
        elif besteed == 13:
            yahtzee()
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
        print("Helaas heeft u nu geen yahtzee, probeer het opnieuw")
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
        dobbel1 = dobbelKiezen()
        dobbel2 = dobbelKiezen()
        dobbel3 = dobbelKiezen()
        dobbel4 = dobbelKiezen()
        dobbel5 = dobbelKiezen()
    print("dobbelsteen 1:", dobbel1)
    print("dobbelsteen 2:", dobbel2)
    print("dobbelsteen 3:", dobbel3)
    print("dobbelsteen 4:", dobbel4)
    print("dobbelsteen 5:", dobbel5)
    
    keep()

    if houden1 == "Y":
        pass
    else:
        dobbel1 = dobbelKiezen()
    if houden2 == "Y":
        pass
    else:
        dobbel2 = dobbelKiezen()
    if houden3 == "Y":
        pass
    else:
        dobbel3 = dobbelKiezen()
    if houden4 == "Y":
        pass
    else:
        dobbel4 = dobbelKiezen()
    if houden5 == "Y":
        pass
    else:
        dobbel5 = dobbelKiezen()


while rondes < 4:
    for i in range(3):
        gooien()
    besteden()
    
print(dobbelscore)