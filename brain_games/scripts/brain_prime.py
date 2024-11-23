import random
from brain_games.cli import welcom_user


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


def game_prime():
    name = welcom_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    run: bool = True
    counter: int = 0

    while run:

        random_num: int = random.randint(1, 100)
        num_prime: bool = is_prime(random_num)
        print(f'Question: {random_num}')

        result: str = input('You answer: ')

        if result == 'yes' or result == 'no':
            if counter < 2:
                if result == 'yes' and num_prime is True:
                    print('Correct!')
                    counter += 1
                    random_num = random.randint(1, 100)
                elif result == 'no' and num_prime is False:
                    print('Correct!')
                    counter += 1
                    random_num = random.randint(1, 100)
                else:
                    print(f"'{result}' is wrong answer ;(. "
                          f"Correct answer was "
                          f"'{'yes' if result == 'no' else 'no'}'.\n"
                          f"Let's try again, {name}!")
                    break
            else:
                print(f'Congratulations, {name}')
                run = False
        else:
            print("entry only 'yes' or 'no'")
            continue
