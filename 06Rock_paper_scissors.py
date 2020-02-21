"""
Gra w papier kamień nożyce
"""

import random

print('Papier, kamień nożyce!')
print('P - papier')
print('K - kamień')
print('N - nożyce')
print('Q - ZAKOŃCZ')

#Opcje wygranej
wins = {'P':'K', 'K':'N', 'N':'P'}

#Możliwe odpowiedzi do wpisania
keys = ['P', 'K', 'N', 'Q']

#Punkty gracza i bota
y_points = 0
bot_points = 0

#Główna pętla gry
while True:
    #Wybór użytkownika
    y_choice = input('Podaj swój wybór (P/K/N/q): ')
    y_choice = y_choice.upper()

    if y_choice not in keys:
        print('Źle wprowadzone dane! Spróbuj jeszcze raz')
        continue

    #Instrukcja zakończenia gry
    if y_choice == 'Q':
        if y_points > bot_points:
            print('Koniec gry, wygrywasz z przewagą ' + str(y_points-bot_points) + ' pkt!')
        else:
            print('Koniec gry, przegrywasz o ' + str(bot_points-y_points) + ' pkt!')
        break

    #Losowanie bota
    bot_choice = random.choice(['P', 'K', 'N'])
    print('Przeciwnik wybrał: ', bot_choice)

    if wins[y_choice] == bot_choice:
        y_points += 1
        print('Wygrałeś! Masz ' + str(y_points) + ' punktów.')
    elif y_choice == bot_choice:
        print('REMIS!')
    elif wins[y_choice] != bot_choice:
        bot_points += 1
        print('Przegrałeś! Bot ma ' + str(bot_points) + ' punktów.')
    else:
        print('Nieprawidłowo podane dane! Spróbuj jeszcze raz')
    print('\n')




