from random import randint

rules = 'What number is missing in the progression?'


def make_progression():
    num = []
    initial_number, difference = randint(0, 50), randint(0, 50)
    length = 10
    for index in range(length):
        initial_number += difference
        num.append(initial_number)

    random_index = randint(0, 9)
    correct_answer = str(num[random_index])
    return num, correct_answer, random_index


def play_game():
    num, correct_answer, random_index = make_progression()
    num[random_index] = '..'
    num = ' '.join(str(i) for i in num)
    return correct_answer, num
