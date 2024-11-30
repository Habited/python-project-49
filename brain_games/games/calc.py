from brain_games.consts import MATHEMATICAL_SYMBOL, CALC, NUMBER_OF_ROUNDS
from brain_games.util import get_random_num, get_random_symbol
from brain_games.engine import run_games


def get_answer_and_question():
    question = (f"{get_random_num()} "
                f"{get_random_symbol(MATHEMATICAL_SYMBOL)} "
                f"{get_random_num()}")
    correct_answer = eval(question)
    return str(correct_answer), question


def run_calc_games():
    return run_games(CALC, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
