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
            if counter != 2:
                if result == 'yes' and number % 2 == 0:
                    print('Correct!')
                    counter += 1
                    number = random.randint(1, 1000)
                elif result == 'no' and number % 2 != 0:
                    print('Correct!')
                    counter += 1
                    number = random.randint(1, 1000)
                else:
                    print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                    print(f"Let's try again, {name}!")
                    break
            else:
                print('Correct!')
                print(f'Congratulations, {name}!')
                run = False
        else:
            print("entry only 'yes' or 'no'")
            continue
