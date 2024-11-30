from brain_games.consts import PRIME, NUMBER_OF_ROUNDS
from random import randint
from brain_games.engine import run_games


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return 'no'
    else:
        return 'yes'


def get_answer_and_question():
    num: int = randint(1, 100)
    question = str(num)
    correct_answer = is_prime(num)
    return str(correct_answer), question


def run_prime_games():
    return run_games(PRIME, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
