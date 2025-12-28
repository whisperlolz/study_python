import random

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
GAMECONTINUE = True
deckCardsPlayer = []
deckCardsDealer = []
deckGame = RANKS.copy()

value_player = 0
value_dealer = 0


# try:
#     startQ = int(input("""
#     $$$$$$$$$$$$$$$$$$$$$$$$$ Welcome to our casino $$$$$$$$$$$$$$$$$$$$$$$$$
#     Chcesz zaczac gre? [Tak-1, Nie-2]
#     Twoj wybor: """))
#     while GAMECONTINUE:
#
# except:
#     print("Musi byc podana 1 lub 2.")

def create_deck(participant, n):
    cards = random.sample(deckGame, n)
    participant.extend(cards)

    for card in cards:
        deckGame.remove(card)


def calculate_hand_value(hand):
    global value_player
    for el in hand:
        if el in ('J', 'Q', 'K'):
            value_player += 10
        elif el == 'A':
            aces_q = int(input("""
Jak chcesz policzyc A jako:
    • 01: wybierz - 1
    • 11: wybierz - 2 
Twoj wybor: """))
            if aces_q == 1:
                value_player += 1
            elif aces_q == 2:
                value_player += 11
        else:
            value_player += el


create_deck(deckCardsPlayer, 2)
print(f"""
Twoje Karty: {deckCardsPlayer}""")
add_deck_q = int(input("""Czy potrzebujesz jeszcze katry? Tak-1, Nie-2
Twoj wybor: """))

if add_deck_q == 1:
    create_deck(deckCardsPlayer, 1)
    print(deckCardsPlayer)
    calculate_hand_value(deckCardsPlayer)
    print(value_player)

elif add_deck_q == 2:
    calculate_hand_value(deckCardsPlayer)
    print(value_player)

create_deck(deckCardsDealer, 2)

print(deckCardsDealer)
a = calculate_hand_value(deckCardsDealer)

print(value_dealer)
