from brain_games.consts import PRIME, NUMBER_OF_ROUNDS
from brain_games.util import get_random_num
from brain_games.engine import run_games


def is_prime(num):
    if num < 2:
        return 'no'
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return 'no'
    else:
        return 'yes'


def get_answer_and_question():
    question = get_random_num()
    correct_answer = is_prime(question)
    return correct_answer, question


def run_prime_games():
    return run_games(PRIME, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
