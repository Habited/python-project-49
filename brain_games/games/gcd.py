from brain_games.consts import GCD, NUMBER_OF_ROUNDS
from random import randint
from brain_games.engine import run_games


def get_gcd(num_1, num_2):
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            return num_1 % num_2
        else:
            return num_2 % num_1


def get_answer_and_question():
    num_1, num_2 = randint(1, 100), randint(1, 100)
    question = f"{num_1} {num_2}"
    correct_answer = get_gcd(num_1, num_2)
    return str(correct_answer), question


def run_gcd_games():
    return run_games(GCD, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
