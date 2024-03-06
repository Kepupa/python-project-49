from random import randint



rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question():
    num = randint(1, 100)
    flag = is_even(num)
    if flag is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, num


def is_even(num):
    return True if num % 2 == 0 else False
    