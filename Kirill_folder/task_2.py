import random as rnd

GAME = True
RND_ITEM = 0
BACKPACK_INIT = ("siekiera", "książki", "ołówek", "skarpetki", "czapka", "pochodnia", "pasta do zębów", "tablet",
                 "latarka", "banan")
lives = 0
backpack_new = []


def loose_life():
    global lives
    global GAME
    lives -= 1
    if lives > 0:
        print(f"Tracisz zycie! Zostalo Ci {lives} zycia(-ie) {"♥" * lives}\nWracasz na korytarz!\n")
        return False
    else:
        print("Nie zostalo ci zdrowia. Koniec gry.")
        GAME = False
        return True


def pokoj_one():
    print("\nWszedłeś do pokoju po lewej!")
    swiatlo = int(input("Czy chcesz zapałić światło [Tak-1/Nie-2]: "))
    if swiatlo == 1:
        print("Swiatlo sie zapalilo ")
        answ = int(input("""
Zauwazasz postać. Co robisz?
Wybierz wariant:
    1. uciekam
    2. podchodze
Twoj wybor to: """))
        if answ == 1:
            print("Uciekasz na korytarz\n")
            return False
        if answ == 2:
            print("Zabiaja cie dziwna postac")
            loose_life()
            return False

    if swiatlo == 2:
        print("Zabija cie ciemnosc")
        loose_life()
    return False


def pokoj_two():
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
            return False


while GAME:
    game_start = int(input("Zaczynamy [Tak-1/Nie-2]: "))
    if game_start == 1:

        while True:
            lives = int(input("Podaj liczbe ile zyc chesz miec: "))
            if lives > 0:
                print(f"Masz {lives} zyc(ia)! {"♥" * lives}")
                break
            else:
                print("Zle podales zycia. Podaj jeszcze raz!")

        while GAME == True and lives > 0:
            direction = int(input("Masz do wyboru 2 pokoje: [Lewy-1 , Prawy-2]: "))

            while True:
                if direction == 1:
                    pokoj_one()
                    break

                if direction == 2:
                    pokoj_two()
                    break

                else:
                    print("Brak takiego pokoju")

    if game_start == 2:
        print("Spierdalaj")
        GAME = False
        break
