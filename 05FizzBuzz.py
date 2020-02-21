"""
Zabawa FizzBuzz zwraca Fizz gdy liczba jest podzielna przez 3, Buzz gdy jest podzielna przez 5 oraz FizzBuzz gdy jest
podzielna przez 3 i 5
"""

for number in range(101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz ', number)
    elif number % 3 == 0:
        print('Fizz ', number)
    elif number % 5 == 0:
        print('Buzz ', number)