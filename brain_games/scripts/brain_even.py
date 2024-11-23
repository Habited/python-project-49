import random
from brain_games.cli import welcom_user


def game_parity_check():
    name = welcom_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    run: bool = True
    counter: int = 0

    while run:
        number: int = random.randint(1, 100)
        print(f'Question: {number}')
        result: str = input('You answer: ')

        if result == 'yes' or result == 'no':
            if counter < 2:
                if result == 'yes' and number % 2 == 0:
                    counter += 1
                    number = random.randint(1, 1000)
                    print('Correct!')
                elif result == 'no' and number % 2 != 0:
                    counter += 1
                    number = random.randint(1, 1000)
                    print('Correct!')
                else:
                    print(f"'yes' is wrong answer ;(. "
                          f"Correct answer was 'no'.\n"
                          f"'Let's try again, {name}!")
                    break
            else:
                run = False
                print(f'Congratulations, {name}')
        else:
            print("entry only 'yes' or 'no'")
            continue
