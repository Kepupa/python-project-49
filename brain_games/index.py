import prompt
from brain_games.cli import welcome_user



def logic(game):
    name = welcome_user()
    print(game.rules)
    attempts = 0 

    while attempts < 3:
        correct_answer, num = game.make_question()
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            attempts += 1

        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f"\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')