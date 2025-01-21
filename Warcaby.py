import random
import colorama
from colorama import Fore, Back, Style, init
init(autoreset=True)
import keyboard
import pyautogui



cursor = [1, 1]

def kolor():
    opcje = ["biały", "czarny"]
    return random.choice(opcje)


def plansza(pole):
    for wiersz in pole:
        print(" ".join(wiersz))
    print("\n")


def czyruchjestpoprawy(Ruch):
    Ruch = int(Ruch)
    if Ruch > 8 or Ruch < 1:
        return 0
    return 1


def czyWspółrzędneSąPoprawne(pole, a, b, gracz):
    a = int(a)
    b = int(b)
    znak = pola[a][b]
    polebezkoloru=  znak.replace("\033[48;2;255;192;203m", "").replace("\033[0m", "")

    if polebezkoloru == gracz:
        return 1
    if gracz == "☖" and polebezkoloru == "♔":
        return 1
    if gracz == '☗' and polebezkoloru == "♚":
        return 1
    else:
        return 0


def ruch(a, b, x, y, pola):
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)
    znak = pola[a][b]
    jasny_rozowy = "\033[48;2;255;192;203m"
    reset = "\033[0m"
    pola[x][y] = f"{jasny_rozowy}{znak}{reset}"
    pola[a][b] = "▒"
    return


def czyDamka(gracz, wiersz, kol, pola):
    znak1 = "♔"
    znak2 ="♚"
    jasny_rozowy = "\033[48;2;255;192;203m"
    reset = "\033[0m"

    wiersz = int(wiersz)
    kol = int(kol)
    if pola[wiersz][kol] == "♔" or pola[wiersz][kol] == "♚":
        return 0

    if gracz == "☖" and wiersz == 8:
        pola[wiersz][kol] = f"{jasny_rozowy}{znak1}{reset}"
        print(Fore.RED + f"gracz {gracz} zdobywa Damkę!")
    if gracz == '☗' and wiersz == 1:
        pola[wiersz][kol] = f"{jasny_rozowy}{znak2}{reset}"
        print(Fore.RED + f"gracz {gracz} zdobywa Damkę!")


def zbiciePionka(pole, a, b, gracz):
    pole[a][b] = "▒"
    global biale
    global czarne
    if gracz == '☗':
        biale = biale - 1
    else:
        czarne = czarne - 1
    return


def czyWspolrzedneSaWolne(pole, a, b, z, z2, gracz, CzyPonownie):
    a = int(a)
    b = int(b)
    z = int(z)
    z2 = int(z2)

    znak1 = pola[z][z2]
    znak2 = pola[a][b]
    poleskad = znak1.replace("\033[48;2;255;192;203m", "").replace("\033[0m", "")
    poledokad = znak2.replace("\033[48;2;255;192;203m", "").replace("\033[0m", "")

    if z2 == b and a != z:
        return 0
    if a == z and b == z2 and CzyPonownie == "1":
        return 1

    if poleskad == "♔" or poleskad == "♚":

        if poledokad == "▒":

            licznikPionkowPoDrodze = 0
            if b > z2:
                kierunek = 1
            else:
                kierunek = -1

            if z > a:
                krok = -1
            else:
                krok = 1

            zmienna = kierunek
            if gracz == '☗':
                for wiersz in range(z + krok, a, krok):
                    if pole[wiersz][z2 + kierunek] == "☖":
                        licznikPionkowPoDrodze += 1

                    if pole[wiersz][z2 + kierunek] == '☗':
                        print(Fore.RED + "Nie można przeskakiwać własnych pionków...")
                        return 0
                    kierunek += zmienna

            if gracz == "☖":
                for wiersz in range(z + krok, a, krok):

                    if pole[wiersz][z2 + kierunek] == '☗':
                        licznikPionkowPoDrodze += 1
                    if pole[wiersz][z2 + kierunek] == "☖":
                        print(Fore.RED + "Nie można przeskakiwać własnych pionków...")
                        return 0
                    kierunek += zmienna

            if licznikPionkowPoDrodze <= 1:
                if CzyPonownie == "2":
                    CanMoveAgain(pole, z, z2, a, b, gracz, CzyPonownie)
                return 1
            else:
                print(Fore.RED + "Damka może przeskoczyć ponad maksymalnie 1 pionkiem przeciwnika!")
                return 0
        else:
            return 0

    if poleskad == "☖" or poleskad == '☗':
        if poledokad == "▒":
            if abs(a - z) == 1:
                return 1
            else:
                if abs(a - z) == 2:
                    if CzyPonownie == "1":
                        return 1
                    else:
                        if CanMoveAgain(pole, z, z2, a, b, gracz, CzyPonownie) == 1:
                            return 1
                        else:
                            return 0
                else:
                    return 0
        else:
            return 0
    else:
        return 0


def CanMoveAgain(pole, a, b, x, y, gracz, czyponownie):
    a = int(a)
    b = int(b)
    x = int(x)
    y = int(y)
    global licznikZbicWRundzie
    if b == y:
        return 0

    znak1 = pola[a][b]
    poleskad = znak1.replace("\033[48;2;255;192;203m", "").replace("\033[0m", "")

    if gracz == '☗' and CzyPonownyRuch=="1" and licznikZbicWRundzie>0:
        if y > b:
            if pole[a - 1][y - 1] == "☖" or pole[a - 1][y - 1] == "♔":
                print(Fore.RED + "zbicie!!!")
                zbiciePionka(pole, a - 1, y - 1, gracz)
                licznikZbicWRundzie += 1
                return 1
            else:
                return 0
        else:
            if pole[a - 1][y + 1] == "☖" or pole[a - 1][y + 1] == "♔":
                print(Fore.RED + "zbicie!!!")
                zbiciePionka(pole, a - 1, y + 1, gracz)
                licznikZbicWRundzie += 1
                return 1
            else:
                return 0

    if gracz == "☖" and CzyPonownyRuch=="1" and licznikZbicWRundzie>0:
        if y > b:

            if pole[a + 1][y - 1] == '☗' or pole[a + 1][y - 1] == "♚":
                print(Fore.RED + "zbicie!!!")
                zbiciePionka(pole, a + 1, y - 1, gracz)
                licznikZbicWRundzie += 1
                return 1
            else:
                return 0
        else:
            if pole[a + 1][y + 1] == '☗' or pole[a + 1][y + 1] == "♚":
                print(Fore.RED + "zbicie!!!")
                zbiciePionka(pole, a + 1, y + 1, gracz)
                licznikZbicWRundzie += 1
                return 1
            else:
                return 0
    else:
        if licznikZbicWRundzie == 0 and czyponownie == "1":
            return 0
        if gracz == '☗':
            dozbicia1 = "☖"
            dozbicia2 = "♔"
        if gracz == "☖":
            dozbicia1 = '☗'
            dozbicia2 = "♚"

        if b > y:
            kierunek = -1
        else:
            kierunek = 1
        zmienna = kierunek

        if a > x:
            krok = -1
        else:
            krok = 1

        for wiersz in range(a + krok, x, krok):
            if pole[wiersz][b + kierunek] == dozbicia1 or pole[wiersz][b + kierunek] == dozbicia2:
                print(Fore.RED + "zbicie!!!")
                zbiciePionka(pole, wiersz, b + kierunek, gracz)
                licznikZbicWRundzie += 1
                return 1
            kierunek += zmienna
        else:
            return 0


pola = [
    [" ", '', '',' ', '', '', '', '', ' '],
    ['', '░', '☖', '░', '☖', '░', '☖', '░', '☖'],
    ['', '☖', '░', '☖', '░', '☖', '░', '☖', '░'],
    ['', '░', '▒', '░', '▒', '░', '▒', '░', '▒'],
    ['', '▒', '░', '▒', '░', '▒', '░', '▒', '░'],
    ['', '░', '▒', '░', '▒', '░', '▒', '░', '▒'],
    ['', '▒', '░', '▒', '░', '▒', '░', '▒', '░'],
    ['', '░', '☗', '░', '☗', '░', '☗', '░', '☗'],
    ['', '☗', '░', '☗', '░', '☗', '░', '☗', '░']

]

pola[1][1] = f"\033[48;2;255;192;203m░\033[0m"


max_y = len(pola) - 1
max_x = len(pola[0]) - 1

def changecolor(cursor,opcja):
    znak = pola[cursor[0]][cursor[1]]
    jasny_rozowy = "\033[48;2;255;192;203m"
    white = "\033[48;5;15m"
    reset = "\033[0m"

    if opcja=="dodaj":
        pola[cursor[0]][cursor[1]] = f"{jasny_rozowy}{znak}{reset}"
        pyautogui.hotkey('alt', 'd')
        plansza(pola)

    if opcja == "usun":
        znak_bez_koloru = znak.replace("\033[48;2;255;192;203m", "").replace("\033[0m", "")
        pola[cursor[0]][cursor[1]] = znak_bez_koloru




def move_cursor(key, cursor, max_x, max_y):
    starycursor = cursor[:]

    if key == "up":
        cursor[0] -= 1
    elif key == "down":
        cursor[0] += 1
    elif key == "left" :
        cursor[1] -= 1
    elif key == "right":
        cursor[1] += 1

    if czyruchjestpoprawy(cursor[0])==0 or czyruchjestpoprawy(cursor[1])==0:
        print(Fore.RED +"niepoprawny ruch")
        cursor[:] = starycursor[:]
        return

    changecolor(starycursor,"usun")
    changecolor(cursor,"dodaj")



def obslugaRuchu():
    global licznikruchow
    licznikruchow+=1
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "up":

                move_cursor("up", cursor, max_x, max_y)
            elif event.name == "down":

                move_cursor("down", cursor, max_x, max_y)
            elif event.name == "left":

                move_cursor("left", cursor, max_x, max_y)
            elif event.name == "right":

                move_cursor("right", cursor, max_x, max_y)

            elif event.name == "enter":
                print(f"Zatwierdzono pole: ({cursor[0]}, {cursor[1]})")
                break

print(Fore.MAGENTA + "WARCABY")
print(Fore.MAGENTA + "---------------------")

odp = input("Wybierz opcję:\n 1 losowanie koloru \n 2 wybór koloru\n")
while odp != "1" and odp != "2":
    print("niepoprawna odpowiedź...\n")
    odp = input("Wybierz opcję:\n 1 - losowanie koloru \n 2 - wybór koloru\n")

if odp == "1":
    gracz1 = kolor()
    if gracz1 == "biały":
        gracz2 = "czarny"
    else:
        gracz2 = "biały"
    print(f"wynik losowania: \ngraczu 1 Twój kolor to {gracz1}! \ngraczu 2 Twój kolor to {gracz2}!")

elif odp == "2":
    odp = input("Wybierz opcję:\n 1 - kolor biały \n 2 - kolor czarny\n")
    while odp != "1" and odp != "2":
        print("niepoprawna odpowiedź...\n")
        odp = input("Wybierz opcję:\n 1 - kolor biały \n 2 - kolor czarny\n")
    if odp == "1":
        gracz1 = "biały"
        gracz2 = "czarny"
    elif odp == "2":
        gracz2 = "biały"
        gracz1 = "czarny"

    print(f"graczu 1 Twój kolor to: {gracz1}!\ngraczu 2 Twój kolor to: {gracz2}!")


print(Fore.MAGENTA + "---------------------")
print(
    "ZASADY\n Gra kończy się gdy wszystkie pionki jednego z graczy zostaną zbite!\n Możesz poruszać się o jedno pole w przód lub w tył\n Nie możesz bić do tyłu\n Możesz bić wielokrotnie pod rząd w jednym ruchu\n Aby wykonać ruch użyj: \n - strzałek do wyboru pionka/pola \n - klawiszu ENTER do zatwierdzenia wyboru ")
print(Fore.MAGENTA + "---------------------")
if gracz1 == "biały":
    print("Rozpoczyna gracz 1\n")


else:
    print("Rozpoczyna gracz 2\n")
gracz = "☖"

# STARTGRY
biale = 8
czarne = 8
licznikZbicWRundzie = 0
CzyPonownyRuch = "2"

while czarne > 0 and biale > 0:
    CzyPrzerwac = "1"
    licznikruchow = 0

    #if licznikZbicWRundzie >= 0:
    if CzyPonownyRuch=="1":
        skad1 = dokad1
        skad2 = dokad2


    if CzyPonownyRuch == "2":
        plansza(pola)

        print(f"Graczu {gracz} wybierz pionek: \n")
        obslugaRuchu()

        skad1 = cursor[0]
        skad2 = cursor[1]

        while czyWspółrzędneSąPoprawne(pola, skad1, skad2, gracz) == 0:
            print("współrzędne są niepoprawne, wybierz je ponownie... \n")

            print(f"graczu {gracz} wybierz pionek: \n")
            obslugaRuchu()
            skad1 = cursor[0]
            skad2 = cursor[1]



    print(f"graczu {gracz} wybierz pole: \n")
    obslugaRuchu()

    dokad1 = cursor[0]
    dokad2 = cursor[1]


    while czyWspolrzedneSaWolne(pola, dokad1, dokad2, skad1, skad2, gracz, CzyPonownyRuch) == 0:
        print("niepoprawne współrzędne\n")
        # wychwytywanie zawartosci z ruchow
        for e in range(licznikruchow):
            input()
            licznikruchow=0

        if CzyPonownyRuch == "2":
            CzyZmianaPionka = input(f"graczu {gracz} chcesz wybrać inny pionek?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")
            while CzyZmianaPionka != "1" and CzyZmianaPionka != "2":
                print("niepoprawna odpowiedź")
                CzyZmianaPionka = input(f"graczu {gracz} chcesz wybrać inny pionek?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")
            if CzyZmianaPionka == "1":
                plansza(pola)
                print(f"graczu {gracz} wybierz pionek: \n")
                obslugaRuchu()
                skad1 = cursor[0]
                skad2 = cursor[1]

                while czyWspółrzędneSąPoprawne(pola, skad1, skad2, gracz) == 0:
                    print("współrzędne są niepoprawne, podaj je ponownie \n")

                    print(f"graczu {gracz} wybierz pionek: \n")
                    obslugaRuchu()
                    skad1 = cursor[0]
                    skad2 = cursor[1]

        print(f"graczu {gracz} wybierz pole: \n")
        obslugaRuchu()

        dokad1 = cursor[0]
        dokad2 = cursor[1]


    while CzyPonownyRuch == "1" and CanMoveAgain(pola, skad1, skad2, dokad1, dokad2, gracz, CzyPonownyRuch) == 0:

        print(Fore.RED + "Aby ruszyć się ponownie, musisz zbić w tym i poprzednim ruchu, niepoprawny ruch")
        #wychwytywanie zawartosci z ruchow
        for e in range(licznikruchow):
            input()
        licznikruchow=0

        CzyPrzerwac = input(f"graczu {gracz}, czy chcesz się ruszyć ponownie?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")
        while CzyPrzerwac != "1" and CzyPrzerwac != "2":
            print("niepoprawna odpowiedź")
            CzyPrzerwac = input(f"graczu {gracz}, czy chcesz się ruszyć ponownie?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")
        if CzyPrzerwac == "2":
            CzyPonownyRuch = "2"
            break

        print(f"graczu {gracz} wybierz pole: \n")
        obslugaRuchu()
        dokad1 = cursor[0]
        dokad2 = cursor[1]

        while czyWspolrzedneSaWolne(pola, dokad1, dokad2, skad1, skad2, gracz, CzyPonownyRuch) == 0:
            print("niepoprawne współrzędne\n")
            print(f"graczu {gracz} wybierz pole: \n")
            obslugaRuchu()

            dokad1 = cursor[0]
            dokad2 = cursor[1]

    if CzyPrzerwac == "1":
        ruch(skad1, skad2, dokad1, dokad2, pola)
        czyDamka(gracz, dokad1, dokad2, pola)
        plansza(pola)
        #wychwytywanie zawartosci z ruchow
        for e in range(licznikruchow):
            input()
            licznikruchow=0
        CzyPonownyRuch = input(f"graczu {gracz}, czy chcesz się ruszyć ponownie?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")
        while CzyPonownyRuch != "1" and CzyPonownyRuch != "2":

            print("niepoprawna odpowiedź")
            CzyPonownyRuch = input(
                f"graczu {gracz}, czy chcesz się ruszyć ponownie?\n odpowiedz:\n 1 - TAK\n 2 - NIE\n")

    if CzyPonownyRuch == "2":
        licznikZbicWRundzie = 0
        if gracz == "☖":
            gracz = '☗'
        else:
            gracz = "☖"

if czarne == 0:
    print("gracz '☗' wygrywa!!!")
else:
    print("gracz '☖' wygrywa!!!")
exit()
