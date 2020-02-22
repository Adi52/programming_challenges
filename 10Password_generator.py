import random

punctation_marks = ['`', '~', '!', '@', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']',
                              '}', ';', ':', '\\', '|', '/', '?', '.', '>', ',', '<', '#', '"', "'"]

letters_upper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
                           'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

letters_lower = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k',
                           'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

x = [punctation_marks, letters_upper, letters_lower, numbers]


while True:
    n = input('Podaj jak długie hasło chcesz (min 6 znaków): ')

    if int(n) > 5:
        break
    else:
        print('Hasło musi mieć minimum 6 znaków!')

password = []

for char in range(int(n)):
    category = random.choices(x)
    password.append(random.choice(category[0]))

print("Propozycja hasła dla Ciebie: ", "".join(password))





