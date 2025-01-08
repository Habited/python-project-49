from math import gcd
from brain_games.consts import GCD
from brain_games.engine import run_games
from brain_games.util import get_random_num


def get_answer_and_question():
    num_1, num_2 = get_random_num(1, 100), get_random_num(1, 100)
    question = f"{num_1} {num_2}"
    correct_answer = gcd(num_1, num_2)
    return str(correct_answer), question


def run_gcd_games():
    return run_games(GCD, get_answer_and_question)
