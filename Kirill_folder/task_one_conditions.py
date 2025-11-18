def swiatlo():
    swiatlo_switch = int(input("""
Czy chesz wlaczyc siatlo [Tak-1 / Nie-2]: """))
    if swiatlo_switch == 1:
        pass
    if swiatlo_switch == 2:
        pass


def pokoj_one():
    print("""
Wszedłeś do prawego pokoju!""")
    swiatlo()


def pokoj_two():
    print("""
Wszedles do lewego pokoju!""")
    swiatlo()


game_start = int(input("""
Siema! Chcesz zacząć gre? [Tak-1 / Nie-2]: """))

if game_start == 1:
    room_choice = int(input("""
Masz do wyboru 2 pokoje
    1. Prawy
    2. Lewy
Twój wybor: """))

    if room_choice == 1:
        pokoj_one()

    if room_choice == 2:
        pokoj_two()

if game_start == 2:
    print("Bye!")
