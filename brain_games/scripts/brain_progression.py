import random

from brain_games.cli import welcom_user


def get_progression() -> list:
    random_value: int = random.randint(1, 10)
    random_step: int = random.randint(1, 10)

    random_list: list = []

    for _ in range(10):
        random_list.append(str(random_value))
        random_value += random_step

    random_elem: int = random.choice(random_list)

    for index, value in enumerate(random_list):
        if value == random_elem:
            random_list[index] = ".."

    return random_list, random_elem


def game_progression():

    name: str = welcom_user()
    print('What number is missing in the progression?')

    run: bool = True
    counter: int = 0

    while run:

        progression: int = get_progression()

        print(f'Question: {' '.join(progression[0])}')
        result: str = input('You answer: ')

        if result.isdigit():
            if counter < 2:
                if result == str(progression[1]):
                    print('Correct!')
                    counter += 1
                else:
                    print(f"'{result}' is wrong answer ;(. "
                          f"Correct answer was '{str(progression[1])}'.\n"
                          f"Let's try again, {name}!")
                    break
            else:
                run = False
                print(f'Congratulations, {name}')
        else:
            print("enter only the number")
            continue
