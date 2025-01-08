from brain_games.consts import PRIME
from brain_games.engine import run_games
from brain_games.util import get_random_num


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


def get_problem_and_answer():
    problem_num = get_random_num(1, 100)
    answer = 'yes' if is_prime(problem_num) else 'no'

    return answer, problem_num


def run_prime_games():
    return run_games(PRIME, get_problem_and_answer)
