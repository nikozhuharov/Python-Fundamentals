deck = input().split()
n = int(input())
half = len(deck)//2
new_deck = []

for i in range (n):

    for j in range(half):
        new_deck.append(deck[j])
        new_deck.append(deck[j+half])
    deck = new_deck
    new_deck = []

print(deck)