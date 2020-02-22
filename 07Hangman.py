import random, time

words = ['zapalniczka', 'rabarabar', 'ziemniak', 'mieszkanie', 'borówka', 'przystań', 'górnik', 'pielgrzymka',
         'plandeka', 'wykałaczka', 'kostka', 'kanapa', 'komputer', 'łazienka', 'motorówka', 'nabrzeże', 'telewizor',
         'podłoga', 'kaloryfer']


cls = lambda: print('\n' * 1000)


def draw_hangman(lifes):
    if lifes == 8:
        print("""

                |     
                |     
                |    
                |    
                |
            """
              )

    if lifes == 7:
        print("""
                 _____
                |     
                |     
                |    
                |     
                |
            """
              )

    if lifes == 6:
        print("""
                 _____
                |     |
                |     
                |    
                |     
                |
            """
              )

    if lifes == 5:
        print("""
                 _____
                |     |
                |     O
                |    
                |    
                |
            """
              )

    if lifes == 4:
        print("""
                 _____
                |     |
                |     O
                |     |
                |     
                |
            """
              )

    if lifes == 3:
        print("""
                 _____
                |     |
                |     O
                |     |
                |    / 
                |
            """
              )

    if lifes == 2:
        print("""
                 _____
                |     |
                |     O
                |     |
                |    / \\
                |
            """
              )

    if lifes == 1:
        print("""
                 _____
                |     |
                |     O
                |    /|
                |    / \\
                |
            """
              )

    if lifes == 0:
        print("""
                 _____
                |     |
                |     O
                |    /|\\
                |    / \\
                |
            """
              )


licznik = 0
active = True

# Główna pętla gry:
while active:

    lifes = 9
    word = list(random.choice(words))
    stan = []
    # Stworzenie pierwszej listy z pierwszą i ostatnią literą, reszta "_"
    stan.append(word[0])

    for i in range(len(word) - 2):
        stan.append('_')
    stan.append(word[-1])

    correct_letters = []
    user_choices_letters = []



    # Pętla konkretnej rozgrywki
    while lifes > 0:
        if licznik == 0:
            print("Zaczynamy!\n")
        licznik += 1

        draw_hangman(lifes)

        if correct_letters:
            print("Już użyłeś: ", ", ".join(user_choices_letters))

        print(" ".join(stan))

        your_choice = input("Podaj literę (wpisz 'quit' aby zakończyć grę): ")

        user_choices_letters.append(your_choice)

        if your_choice == 'quit' or your_choice == 'Quit':
            active = False
            break

        t = [i for i, x in enumerate(word) if x == your_choice and x not in correct_letters]

        time.sleep(2)
        if t:
            for a in t:
                stan[a] = your_choice
            correct_letters.append(your_choice)
            print('Dobrze!')

        else:
            lifes -= 1
            print('Źle!')

        if stan == word:
            cls()
            licznik = 0
            print('\nBRAWO, WYGRAŁEŚ!\n')
            break

        time.sleep(1)
        cls()