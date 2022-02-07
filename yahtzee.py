import random
dobbel1 = 0
dobbel2 = 0
dobbel3 = 0
dobbel4 = 0
dobbel5 = 0

#--dobbelstenen houden--#
houden1 = "Y"
houden2 = "Y"
houden3 = "Y"
houden4 = "Y"
houden5 = "Y"

def dobbelKiezen():
    getalkiezen = random.randint(1,6)
    return getalkiezen

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

def gooien():
    global dobbel1
    global dobbel2
    global dobbel3
    global dobbel4
    global dobbel5
    
    input("Druk op enter om de dobbelstenen te gooien")
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
gooien()