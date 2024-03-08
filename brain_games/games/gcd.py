from random import randint
from math import gcd



rules = 'Find the greatest common divisor of given numbers.'


def play_game():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    correct_answer = str(gcd(number_1, number_2))
    num = f'{number_1} {number_2}'

    return correct_answer, num