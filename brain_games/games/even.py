from brain_games.consts import EVEN, NUMBER_OF_ROUNDS
from brain_games.util import get_random_num
from brain_games.engine import run_games


def is_even(num):
    return num % 2 == 0


def get_answer_and_question():
    question: int = get_random_num()
    correct_answer: str = 'yes' if is_even(question) else 'no'
    return correct_answer, question


def run_even_games():
    return run_games(EVEN, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
