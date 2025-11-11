lives = 0
GAME = True


def lose_life():
    global lives
    global GAME
    lives -= 1
    if lives > 0:
        print(f"Tracisz zycie! Zostalo Ci {lives} zyc(-ie)!")
    else:
        print("Nie masz wiecej zyc! Przegrales!")
        GAME = False
        return True


def pokoj1():
    global lives
    print("\nWszedłeś do pokoju!")
    swiatlo = input("Czy chcesz zapałić światło [tak/nie]: ").lower().strip()
    if swiatlo == "tak":
        print("Swiatlo sie zapalilo , zauwazam w rogu jakas postac...")

        return False

    if swiatlo == "nie":
        print("Zabija cie ciemnosc")
        return lose_life()


def pokoj2():
    global lives
    answ = int(input("""
Co robisz?
Wybierz wariant:
    - uciekam: 1
    - podchodze: 2
"""))
    if answ == 1:
        print("Uciekam do lazienki")
        return False
    if answ == 2:
        print("Zabiaja cie dziwna postac")
        return lose_life()


## Start
while GAME:
    game_start = input(
        """Siema! Czy chcesz zaczac gre [Tak/Nie]: """).lower().strip()
    if game_start == 'tak':
        lives = int(input("Podaj liczbe ile zyc chesz miec: "))
        print(f"Masz {lives} zyc(-ie)! {"♥" * lives}")

        while lives > 0:
            if pokoj1():
                break
            if pokoj2():
                break
            if lives <= 0:
                break

    if game_start == 'nie':
        GAME = False
        print("Spierdalaj")
