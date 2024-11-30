from brain_games.consts import GCD, NUMBER_OF_ROUNDS
from brain_games.util import get_random_num
from brain_games.engine import run_games
from math import gcd


def get_answer_and_question():
    num_1, num_2 = get_random_num(), get_random_num()
    question = f"{num_1} {num_2}"
    correct_answer = gcd(num_1, num_2)
    return str(correct_answer), question


def run_gcd_games():
    return run_games(GCD, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
