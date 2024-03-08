from random import randint
from math import sqrt

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


def play_game():
    num = randint(1, 100)
    attempts = is_prime(num)
    if attempts is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num