import random
from brain_games.cli import welcom_user
import math


def game_gcd():
    name = welcom_user()
    print('Find the greatest common divisor of given numbers.')

    run: bool = True
    counter: int = 0

    while run:

        random_number_1: int = random.randint(1, 100)
        random_number_2: int = random.randint(1, 100)

        print(f'Question: {random_number_1} {random_number_2}')

        gcd: int = math.gcd(random_number_1, random_number_2)
        result: str = input('You answer: ')

        if result.isdigit():
            if counter < 2:
                if int(result) == gcd:
                    print('Correct!')
                    counter += 1
                else:
                    print(f"'{result}' is wrong answer ;(. "
                          f"Correct answer was '{str(gcd)}'.\n"
                          f"Let's try again, {name}!")
                    break
            else:
                run = False
                print(f'Congratulations, {name}')
        else:
            print("enter only the number")
            continue
