lijstje = {}

def snapNiet():
    print("Sorry, dat snap ik niet... ")

def add():
    toevoegen = input("Wat wil je aan het lijstje toevoegen? ").lower()
    if toevoegen in lijstje:
        lijstje[toevoegen] += 1
    else:
        lijstje[toevoegen] = 1
    meer = input("Wil je nog meer bestellen? ").upper()
    if meer == "JA" or meer  ==  "J":
        add()
    elif meer == "NEE" or meer == "N":
        print("Bedankt voor uw bestelling! ")
        print(lijstje)
        exit()
    else:
        snapNiet()
        add()
    return lijstje
    
add()
print(lijstje)
