from random import randint
from math import gcd


rules = 'Find the greatest common divisor of given numbers.'

def play_game():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    correct_answer = str(gcd(num_1, num_2))
    num = f'{num_1} {num_2}'

    return correct_answer, num