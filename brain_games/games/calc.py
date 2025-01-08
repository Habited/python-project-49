from brain_games.consts import CALC
from brain_games.engine import run_games
from random import choice
from brain_games.util import get_random_num


def get_random_math_sign_and_result(first_num, second_num):
    return choice([('+', first_num + second_num),
                   ('-', first_num - second_num),
                   ('*', first_num * second_num),
                   ])


def get_math_question_and_result():
    first_num, second_num = get_random_num(1, 100), get_random_num(1, 100) 
    sign, result = get_random_math_sign_and_result(first_num, second_num)
    question = f"{first_num} {sign} {second_num}"
    return str(result), question


def run_calc_games():
    return run_games(CALC, get_math_question_and_result)
