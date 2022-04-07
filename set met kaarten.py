import random
bestaandeKleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
soorten = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]
special = ["joker", "joker"]
deck = []
shuffledDeck = []

for i in range(len(bestaandeKleuren)):
    for x in range(len(soorten)):
        deck.append(bestaandeKleuren[i] + " " + soorten[x])
for l in range(len(special)):
    deck.append(special[l])
for i in range(len(deck)):
    randomCard = random.choice(deck)
    deck.remove(randomCard)
    shuffledDeck.append(randomCard)


for i in range(7):
    print(f"kaart {i+1}:",shuffledDeck[0])
    del shuffledDeck[0]

print("Deck (47 kaarten):",shuffledDeck)