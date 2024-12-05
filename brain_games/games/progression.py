from random import choice, randint

from brain_games.consts import NUMBER_OF_ROUNDS, PROGRESSION
from brain_games.engine import run_games


def get_progression_and_elem():
    progression: list = []
    elem_prog: int = randint(1, 100)
    step_prog: int = randint(1, 10)

    for _ in range(randint(5, 10)):
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
    return run_games(PROGRESSION, NUMBER_OF_ROUNDS,
                     get_answer_and_question)
