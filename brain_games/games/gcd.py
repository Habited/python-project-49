from math import gcd
from brain_games.consts import GCD, NUMBER_OF_ROUNDS
from brain_games.engine import run_games
from random import randint


def get_answer_and_question():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    question = f"{num_1} {num_2}"
    correct_answer = gcd(num_1, num_2)
    return str(correct_answer), question


def run_gcd_games():
    return run_games(GCD, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
