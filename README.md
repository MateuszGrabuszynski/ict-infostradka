For our own convenience, documentation of this project will only be held in Polish. At least, until we decide otherwise.

# Infostradka
Projekt zintegrowanego systemu wyświetlaczy informacyjnych opartych o komputery jednopłytkowe Raspberry Pi, realizowany w ramach zajęć projektowych z Podstaw telekomunikacji.

## Przygotowania
### Klient
Aby przygotować Raspberry Pi do poprawnego działania w systemie należy kolejno:
1. Pobrać ze strony https://www.raspberrypi.org/downloads/raspbian/ pełną wersję systemu Raspbian (with desktop);
2. Poprzez program Etcher, bądź inny służący do tego celu, zgrać pobrany obraz płyty na kartę microSD;
3. Uruchomić Raspberry Pi z włożoną kartą microSD i wykonać następujące kroki:
   1. Otworzyć terminal (Ctrl+Alt+T);
   2. Wpisać `sudo raspi-config`;
      1. W zakładce 5 (Interfacing Options) przejść do P2 (SSH) i uruchomić obsługę protokołu. Pomoże to w późniejszej konfiguracji ustawień;
      2. W zakładce 7 (Advanced Options) przejść do A2 (Overscan) i wyłączyć tą opcję;
      3. Wyjść z menu klawiszem Esc;
   3. Wpisać `sudo apt-get update` i poczekać na zakończenie pobierania;
   4. Wpisać `sudo apt-get upgrade -y` i poczekać na zakończenie instalacji;
   5. Zainstalować odpowiednie programy poleceniem `sudo apt-get install chromium-browser x11-xserver-utils unclutter`. Może pojawić się monit o przerwaniu instalacji niektórych programów ze względu na wcześniejsze ich posiadanie, należy to zignorować;
   6. Przygotować odpowiedni plik autostartu:
      1. Wpisać `nano ~/.config/lxsession/LXDE-pi/autostart`;
      2. Zamienić zawartość pliku na następującą (dostępna w pliku autostart):
           
           ```bash
           @lxpanel --profile LXDE
           @pcmanfm --desktop --profile LXDE  
           @xset s off  
           @xset -dpms   
           @xset s noblank
           @sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/chromium Default/Preferences
           @chromium-browser --noerrdialogs --kiosk --incognito --disable-translate [URL_serwera_głównego!]
           ```
     
   7. Dodać odpowiednie zmienne konfiguracyjne w pliku (obecnie nie istnieje na repozytorium);
   8. Zrestartować Raspberry Pi poleceniem `sudo reboot now`.  

Po zrestartowaniu urządzenia na monitorze powinna się wyświetlić odpowiednia strona. Pierwsze pobieranie paczek informacji z serwera może trwać kilka minut. Jeśli jednak po kilku minutach urządzenie nadal wyświetla biały ekran bądź wyświetli się komunikat "Aw, snap!" ze znajomym dinozaurem - należy w pierwszej kolejności sprawdzić połączenie internetowe (polecenia `ifconfig` oraz `ping`), a następnie podane URL serwera i dane konfiguracyjne w pliku.  

Zaczerpnięto z pewnymi zmianami z https://github.com/elalemanyo/raspberry-pi-kiosk-screen

### Serwer
Po przejściu w konsoli do folderu z serwerem należy podać następujące komendy:  
`export FLASK_APP=infostradka.py` dla systemu Windows lub `set FLASK_APP=infostradka.py` dla systemu Linux, i dalej `python -m flask run --host=0.0.0.0`.

## Ograniczenia
System w fazie developerskiej - odnajdowane ograniczenia będą dodawane na bieżąco.

## Autorzy
* Mateusz Norel
* Tomasz Walczak
* Mateusz Grabuszyński

## Ostatnia zmiana
2018-03-29 14:13
