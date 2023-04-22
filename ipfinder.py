import random
import time
import colorama
import sys
from os import system, name
from time import sleep
from colorama import Fore, Back, Style
colorama.init()
import time
import random

print(Fore.RED + "                       ██▒   █▓▓█████   ▄████  ▄▄▄      ▒██   ██▒▒███████▒▓██   ██▓")
print("                       ▓██░   █▒▓█   ▀  ██▒ ▀█▒▒████▄    ▒▒ █ █ ▒░▒ ▒ ▒ ▄▀░ ▒██  ██▒")
print("                        ▓██  █▒░▒███   ▒██░▄▄▄░▒██  ▀█▄  ░░  █   ░░ ▒ ▄▀▒░   ▒██ ██░")
print("                         ▒██ █░░▒▓█  ▄ ░▓█  ██▓░██▄▄▄▄██  ░ █ █ ▒   ▄▀▒   ░  ░ ▐██▓░")
print("                          ▒▀█░  ░▒████▒░▒▓███▀▒ ▓█   ▓██▒▒██▒ ▒██▒▒███████▒  ░ ██▒▓░")
print("                          ░ ▐░  ░░ ▒░ ░ ░▒   ▒  ▒▒   ▓▒█░▒▒ ░ ░▓ ░░▒▒ ▓░▒░▒   ██▒▒▒")
print("                         ░ ░░   ░ ░  ░  ░   ░   ▒   ▒▒ ░░░   ░▒ ░░░▒ ▒ ░ ▒ ▓██ ░▒░")
print("                           ░░     ░   ░ ░   ░   ░   ▒    ░    ░  ░ ░ ░ ░ ░ ▒ ▒ ░░")
print("                            ░     ░  ░      ░       ░  ░ ░    ░    ░ ░     ░ ░")
print()
print()

words = "                                       Made by vegaxzy#7777"
for char in words:
    sleep(0.05)
    sys.stdout.write(char)
print()
print()
print()

# Pobieramy kod, który użytkownik podaje jako login
kod = input('Podaj kod logowania: ')

# Jeśli podany kod jest poprawny...
if kod == '404404':
    # Otwieramy plik do odczytu
    with open('text_file.txt') as f:
        # Pętla, która umożliwia wielokrotne wyszukiwanie wartości w pliku
        while True:
            # Pobieramy wartość, którą użytkownik chce wyszukać
            wartosc = input('Podaj szukany nick (lub "koniec", aby zakończyć): ')

            # Jeśli użytkownik wpisał "koniec"...
            if wartosc == 'koniec':
                # Kończymy pętlę i program
                break

            # Zmienna, która będzie przechowywać informację, czy wartość została znaleziona
            znaleziono = False

            # Dla każdej linii w pliku...
            for linia in f:
                # Jeśli wartość znajduje się w linii...
                if wartosc in linia:
                    # Wyświetlamy całą linię
                    print(linia)
                    # Ustawiamy flagę, że wartość została znaleziona
                    znaleziono = True

            # Jeśli po przejrzeniu wszystkich linii wartość nie została znaleziona...
            if not znaleziono:
                # Wyświetlamy odpowiednią wiadomość
                print('Nie znaleziono podanego ip.')

            # Przesuwamy "wskaznik" na początek pliku (aby móc wielokrotnie przeszukać go od początku)
            f.seek(0)

# Jeśli podany kod jest niepoprawny...
else:
    # Wyświetlamy odpowiednią wiadomość
    print('Niepoprawny kod logowania.')