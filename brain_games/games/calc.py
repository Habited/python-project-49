from brain_games.consts import MATHEMATICAL_SYMBOL, CALC, NUMBER_OF_ROUNDS
from random import randint, choice
from brain_games.engine import run_games


def get_random_simbol():
    return choice(MATHEMATICAL_SYMBOL)


def get_answer_and_question():
    question = f"{randint(1, 100)} {get_random_simbol()} {randint(1, 100)}"
    correct_answer = eval(question)
    return str(correct_answer), question


def run_calc_games():
    return run_games(CALC, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
