from random import choice
from brain_games.util import get_random_num
from brain_games.consts import PROGRESSION
from brain_games.engine import run_games


def get_progression_and_elem():
    progression: list = []
    elem_prog: int = get_random_num(1, 100)
    step_prog: int = get_random_num(1, 10)

    for _ in range(get_random_num(5, 10)):
        progression.append(str(elem_prog))
        elem_prog += step_prog

    rand_elem_prog: str = str(choice(progression))

    for index, value in enumerate(progression):
        if value == rand_elem_prog:
            progression[index] = ".."

    progression = " ".join(progression)

    return progression, rand_elem_prog


def get_answer_and_question():
    question, answer = get_progression_and_elem()
    return answer, question


def run_progression_games():
    return run_games(PROGRESSION, get_answer_and_question)
