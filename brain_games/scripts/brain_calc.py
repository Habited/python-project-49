import random
from brain_games.cli import welcom_user


def choice() -> str:
    simbols: list = ['+', '-', '*']
    simbol: str = random.choice(simbols)
    return simbol


def game_logic_calculator():
    name = welcom_user()
    print('What is the result of the expression?')
    
    run: bool = True
    counter = 0

    while run:
        number_1: int = random.randint(1, 100)
        number_2: int = random.randint(1, 100)
        random_simbol: str = choice() 
        print(f'Question: {number_1} {random_simbol} {number_2}')
        result: str = input('You answer: ')
        
        if result == 'yes' or result == 'no':        
            if result == 'yes' and number % 2 == 0:
                counter += 1
                number = random.randint(1, 1000)
                print('Correct!') 
            elif result == 'no' and number % 2 != 0:
                counter += 1
                number = random.randint(1, 1000)
                print('Correct!')
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!'")
                break
            if counter == 3:
                run = False
                print(f'Congratulations, {name}') 
        else:
            print("entry only 'yes' or 'no'")
            continue

