from random import randint

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def play_game():
    num = randint(2, 99)
    attempts = is_prime(num)
    if attempts is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num