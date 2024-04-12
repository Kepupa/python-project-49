from random import randint, choice
from operator import add, sub, mul

rules = 'What is the result of the expression?'

operators = {
    '+': add,
    '-': sub,
    '*': mul
}


def play_game():
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    operator = choice(list(operators.keys()))
    correct_answer = str(abs(operators[operator](first_number, second_number)))
    if first_number > second_number:
        num = f'{first_number} {operator} {second_number}'
    if first_number == second_number:
        num = f'{first_number} {operator} {second_number}'
    elif second_number > first_number:
        num = f'{second_number} {operator} {first_number}'
    return correct_answer, num
