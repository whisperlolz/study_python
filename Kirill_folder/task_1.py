import random as rnd

GAME = True
RND_ITEM = 0
BACKPACK_INIT = ["siekiera", "książki", "ołówek", "skarpetki", "czapka", "pochodnia", "pasta do zębów", "tablet",
                 "latarka", "banan"]

lives = 0
backpack_new = []


def lose_life():
    global lives
    global GAME
    lives -= 1
    if lives > 0:
        print(f"~ Tracisz zycie! Zostalo Ci {lives} zyc(-ie)! {"♥" * lives} ")
    else:
        print("Nie masz wiecej zyc! Przegrales!")
        GAME = False
        return True


def packing_backpack():
    global BACKPACK_INIT
    global backpack_new
    print("""
    ##################################################
    Dawaj zlozymy plecak. 
    Mozesz dodac 4 rzeczy z listy [twoj wybor jest wazny]:
        - 1. siekiera
        - 2. książki
        - 3. ołówek
        - 4. skarpetki
        - 5. czapka
        - 6. pochodnia
        - 7. pasta do zębów
        - 8. tablet
        - 9. latarka
        - 10. banan
    ##################################################
    """)
    for el in range(4):
        while True:
            num = int(input(f"Prosze podaj {el + 1} element (1–10): "))
            if 0 < num < 11:
                backpack_new.append(BACKPACK_INIT[num - 1])
                print(f"~ Dodales {BACKPACK_INIT[num - 1]} do plecaka. W plecaku juz masz {backpack_new}")
                break  # выходим из внутреннего while, переходим к следующему el
            else:
                print("~ Brak takiej cyfry! Prosze podaj poprawnie.")
        if len(backpack_new) == 4:
            print(f"Plecak masz uzupelniony! Lecimy z koksem")
            break


def pokoj1():
    global lives
    while True:
        print("\nWszedłeś do pokoju!")
        swiatlo = int(input("Czy chcesz zapałić światło [Tak-1 / Nie-2]: "))
        if swiatlo == 1:
            print("Swiatlo sie zapalilo!")
            return False

        if swiatlo == 2:
            print("Zabija cie ciemnosc")
            return lose_life()
            break
        else:
            print("~ Brak takiej cyfry! Prosze podaj poprawnie.")


def pokoj2():
    global lives
    while True:
        answ = int(input("""
    Zauwazam w rogu jakas postac... Co robisz?
    Wybierz wariant:
        - 1. uciekam
        - 2. podchodze
        - 3. wyciagnas przedmiot z plecaka
    Twoj wybor: """))
        if answ == 1:
            print("Uciekam do lazienki")
            return False
        if answ == 2:
            print("Zabiaja cie dziwna postac")
            return lose_life()
        if answ == 3:
            print("... zzzzzZZZZZzzzzz ...")
            while True:
                RND_ITEM = rnd.randint(0, 4)
                # print(RND_ITEM)
                print(f"Wyciagnales {backpack_new[RND_ITEM]}")
                if backpack_new[RND_ITEM] == "siekiera":
                    print("Postac ucieka .... jestes szczesciara!")
                    return False
                if backpack_new[RND_ITEM] == "pochodnia":
                    print("Postac ucieka .... jestes szczesciara!")
                    return False
                else:
                    return lose_life()
            break
        else:
            print("~ Brak takiej cyfry! Prosze podaj poprawnie!")

    ## Start


while GAME:
    game_start = int(input(
        """\nSiema! Czy chcesz zaczac gre [Tak-1 / Nie-2]: """))
    if game_start == 1:
        lives = int(input("Podaj liczbe ile zyc chesz miec: "))
        print(f"Masz {lives} zyc(-ia)! {"♥" * lives}")

        packing_backpack()

        while lives > 0:
            if pokoj1():
                break
            if pokoj2():
                break
            if lives <= 0:
                break

    if game_start == 2:
        GAME = False
        print("Spierdalaj")

# todo 1: dodac powtorke jezeli user podal litere zamiast cyfr. (try ....)
# todo 2: dodac koncowki gry
# todo 3: dodac super gre gry zostaje 1 zycie.
