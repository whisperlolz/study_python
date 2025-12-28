import random


class Game:
    BACKPACK = ("siekiera", "książki", "ołówek", "skarpetki", "czapka", "pochodnia", "pasta do zębów", "tablet",
                "latarka", "banan")

    GOOD_ITEMS = ("siekiera", "pochodnia", "latarka", "banan")

    def __init__(self):
        self.lives = 0
        self.running = True

    def get_choice(self, prompt, valid):
        while True:
            try:
                choice = int(input(prompt))
                if choice in valid:
                    return choice
                print(f"-> Wpisz {valid}")

            except ValueError:
                print("-> To nie jest liczba.")

    def get_positive_int(self, prompt):
        while True:
            try:
                choice = int(input(prompt))
                if choice > 0:
                    return choice
                print("-> Liczba musi być większa od 0.")

            except ValueError:
                print("-> To nie jest liczba.")

    def lose_life(self):
        self.lives -= 1
        if self.lives > 0:
            print(f"Tracisz życie! Zostało: {self.lives}", self.lives * '♥')
        else:
            print("Nie zostało Ci zdrowia. Koniec gry.")
            self.running = False

    def light_action(self):
        choice = self.get_choice("Czy chcesz zapalić światło [1-tak / 2-nie]: ", (1, 2))
        if choice == 2:
            print("Zabija cię ciemność!")
            self.lose_life()
            return False
        else:
            print("Światło się zapaliło!")
            return True

    # ---------- Rooms ----------
    def room_one(self):
        print("<------------------------>\nWitamy w pierwszym pokoju!")

        if not self.light_action():
            return None

        choice = self.get_choice(
            f"""
Zauwazasz postać. Co robisz?
    1.Uciekam
    2.Podchodze
Twoj wybor: """,
            (1, 2))
        if choice == 2:
            print("Zabija cię dziwna postać...")
            self.lose_life()
        else:
            print("Uciekasz na korytarz")

    def room_two(self):
        print("<------------------------>\nWitamy w drugim pokoju!")

        if not self.light_action():
            return None

        choice = self.get_choice(
            f"""
W pokoju leży plecak. Co zrobisz?
    1.Zakładam
    2.Omijam
Twój wybór: """,
            (1, 2))
        if choice == 2:
            print("""
Przechodzisz w środek pokoju...
Spotkało Cie zło!
Nie masz nic żeby bronić się.""")
            self.lose_life()
        else:
            print(
                """
Przechodzisz w środek pokoju...
Spotkało Cie zło!
Musisz wyciągnąć właściwy przedmiot z plecaka żeby obronić się...""")
            get_item = random.choice(self.BACKPACK)
            print("Wyciągasz:", get_item)
            if get_item not in self.GOOD_ITEMS:
                print("\nNiestety nie masz farta. Zło Cie pokonało!")
                self.lose_life()
            else:
                print(
                    f"""
Gratuluje! Pokonaleś Zło
Zostało: {self.lives} {self.lives * "♥"} żyć(-cia).
Wracasz na korytarz!""")

    def room_three(self):
        print("<------------------------>\nWitamy w trzecim pokoju!")

        if not self.light_action():
            return None

        print("""
☻ Niespodzianka ☻
Trafiłeś do ZUS.
Pracownik ZUS chcę zagrać z Tobą!
Musisz zgadnąć, które opodatkowanie pracownik wybierze.
    1. 0% podatku
    2. 50% podatku
    3. 100% podatku
Jeżeli trafisz -> wygrywasz.
Jeżeli nie trafisz -> wygrywa pracownik.
Gramy do 3 wygranych.""")

        game_zus_score_user = 0
        game_zus_score_employee = 0

        while game_zus_score_user != 3 and game_zus_score_employee != 3:
            user_num_choice = self.get_choice(
                "\nPodaj liczbę od 1 do 3: ",
                (1, 2, 3))
            ran_num_employee = random.randint(1, 3)

            if user_num_choice == ran_num_employee:
                game_zus_score_user += 1
                print(f"""
Pracownik wybiera: {ran_num_employee}
Udało się. Ta runda za tobą.
• Masz: {game_zus_score_user} punkty
• Pracownik ma: {game_zus_score_employee} punkty""")

            else:
                game_zus_score_employee += 1
                print(f"""
Pracownik wybiera: {ran_num_employee}
Pracownik wygrywa runde. 
• Masz: {game_zus_score_user} punkty
• Pracownik ma: {game_zus_score_employee} punkty""")

        if game_zus_score_user == 3:
            print("Wygrałeś! Uciekasz od ZUS i nie płacisz nic!\nWracasz na korytarz!")

        if game_zus_score_employee == 3:
            print("Przegrałeś. ZUS zabiera życie!")
            self.lose_life()

    # ---------- Game ----------
    def start(self):
        print("<----- WITAJ W GRZE ----->")
        self.lives = self.get_positive_int("Podaj liczbę, ile żyć chcesz mieć: ")
        print(f"Masz {self.lives} zyc(-ia)! {self.lives * '♥'}")
        while self.running and self.lives > 0:
            choice = self.get_choice(
                """<------------------------>
Masz do wyboru 3 pokoje - wybierz w który chcesz wejść:
    1. Pokój 1
    2. Pokój 2
    3. Pokój 3
Twój wybór to: """,
                (1, 2, 3))
            if choice == 1:
                self.room_one()
            elif choice == 2:
                self.room_two()
            else:
                self.room_three()


# ---------- Start ----------
game = Game()
game.start()
