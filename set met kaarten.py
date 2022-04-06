import random
bestaandeKleuren = ['harten', 'klaveren', 'schoppen', 'ruiten', 'joker']
soorten = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
deck = []
jokers = 2

for i in range(47):
    cardColor = random.choice(bestaandeKleuren)
    cardNumber = random.choice(soorten)
    if cardColor == "joker" and jokers > 0:
        jokers -= 1
        deck.append(cardColor)
    elif cardColor == 'joker' and jokers == 0:
        i -= 1
    else:
        toevoegen = cardColor, cardNumber
        deck.append(toevoegen)

for i in range(7):
    print(deck[i])

print(deck) 