from brain_games.configure import EVEN, NUMBER_OF_ROUNDS
from random import randint
from brain_games.engine import run_games


def is_even(num):
    return num % 2 == 0


def get_answer_and_player_responce():
    num: int = randint(1, 100)
    yes_or_no_answer: str = 'yes' if is_even(num) else 'no'
    player_responce: str = input(f'Question: {num}\nYour answer: ')
    return yes_or_no_answer, player_responce


def run_even_games():
    print()
    return run_games(EVEN, NUMBER_OF_ROUNDS,
                     get_answer_and_player_responce)
