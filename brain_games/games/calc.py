from brain_games.consts import CALC, NUMBER_OF_ROUNDS
from brain_games.engine import run_games
from random import choice, randint


def get_random_math_sign_and_result(first_num, second_num):
    return choice([('+', first_num + second_num),
                   ('-', first_num + second_num),
                   ('*', first_num + second_num),
                   ])


def get_math_question_and_result():
    first_num, second_num = randint(1, 100), randint(1, 100)
    sign, result = get_random_math_sign_and_result(first_num, second_num)
    question = f"{first_num} {sign} {second_num}"
    return question, str(result)


def run_calc_games():
    return run_games(CALC, NUMBER_OF_ROUNDS,
                     get_math_question_and_result)
