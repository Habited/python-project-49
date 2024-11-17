import random
from brain_games.cli import welcom_user


def choice() -> str:
    simbols: list = ['+', '-', '*']
    simbol: str = random.choice(simbols)
    return simbol


def game_calc():
    name = welcom_user()
    print('What is the result of the expression?')

    run: bool = True
    counter: int = 0
    true_answer: int = 0

    while run:

        random_number_1: int = random.randint(1, 100)
        random_number_2: int = random.randint(1, 100)
        random_simbol: str = choice()

        print(f'Question: {random_number_1} {random_simbol} {random_number_2}')

        if random_simbol == '+':
            true_answer = random_number_1 + random_number_2
        elif random_simbol == '-':
            true_answer = random_number_1 - random_number_2
        else:
            true_answer = random_number_1 * random_number_2
        result: str = input('You answer: ')

        if result.isdigit():
            if counter < 2:
                if int(result) == true_answer:
                    print('Correct!')
                    counter += 1
                else:
                    print(f"{result} is wrong answer ;(. "
                          f"Correct answer was {str(true_answer)}.\n"
                          f"Let's try again, {name}!'")
                    break
            else:
                run = False
                print(f'Congratulations, {name}')
        else:
            print("enter only the number")
            continue
