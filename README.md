# 🏁 Gra w Warcaby 

## 🎮 Zasady gry

- Gra toczy się na planszy 8x8, z pionkami poruszającymi się po ciemnych polach, **do przodu lub do tyłu**.
- Gracze mają możliwość **wielokrotnego bicia** przeciwnika.
- Pionki, które dotrą do ostatniej linii planszy, zamieniają się w **damki**, które mają **dodatkowe możliwości poruszania się**.
- Gra kończy się, gdy wszystkie pionki jednego z graczy zostaną zbite.

---

## 🛠 Informacje o programie

- Użytkownik porusza się po planszy za pomocą **strzałek na klawiaturze.**(Biblioteka:**keyboard**)
- o wybraniu pola, gracz zatwierdza swój ruch klawiszem **"Enter"**.
- **Aktualnie wybrane pole jest podkreślane kolorem**, aby użytkownik mógł łatwo zobaczyć, które pole jest zaznaczone.
- Część komunikatów programu wyświetlana jest w **różnych kolorach, co ułatwia orientację i zwiększa przejrzystość interfejsu**. (Biblioteka: **colorama**)
- **Każdy ruch jest weryfikowany**. Użytkownik otrzymuje **informację zwrotną** w przypadku, gdy ruch, wybrane pole lub pionek są niepoprawne.
- Jeśli użytkownik popełni błąd, otrzymuje **opcję zmiany wybranego pionka lub anulowania akcji.**
- **Czyszczenie ekranu**: Ekran jest czyszczony za pomocą biblioteki **pyautogui**, połączonej z wybranym **skrótem klawiszowym**, aby zapewnić płynność rozgrywki.

---

## 🖥 Technologie

- **Python** – język programowania, w którym została zaimplementowana logika gry.
- **keyboard** – biblioteka umożliwiająca wykrywanie naciśnięć klawiszy, umożliwiająca poruszanie się po planszy za pomocą strzałek i zatwierdzanie ruchu przyciskiem "Enter".
- **pyautogui** – biblioteka do automatyzacji GUI, używana do czyszczenia ekranu w trakcie rozgrywki.
- **colorama** – biblioteka do kolorowania tekstów w terminalu, używana do wyświetlania kolorowych komunikatów w grze.

---

## 🚀 Sposób uruchomienia

1. **Pobierz plik z programem**: Pobierz plik z programem i zapisz go na swoim komputerze.
2. **Uruchom program w PyCharm**:
   - Otwórz program **PyCharm** (lub inny edytor kodu, jeśli wolisz).
   - Załaduj pobrany plik projektu.
   - Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki. Możesz je zainstalować za pomocą poniższych komend:
   
     ```bash
     pip install keyboard pyautogui colorama
     ```

3. **Uruchom grę**:
   - Po przygotowaniu środowiska, uruchom program w PyCharm klikając **Run** (lub skrótem klawiszowym **Shift + F10**).
   - Gra zostanie uruchomiona w terminalu, gdzie będziesz mógł rozpocząć rozgrywkę.

---


