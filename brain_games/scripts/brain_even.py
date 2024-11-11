#!/usr/bin/env python3
import random
from brain_games.cli import welcom_user


def get_a_number():
    name = welcom_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    run: bool = True
    counter = 0

    while run:
        number: int = random.randint(1, 100)
        print(f'Question: {number}')
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
                print("'yes' is wrong answer ;(. Correct answer was 'no'.\n", "Let's try again, Bill!'")
                break
            if counter == 3:
                run = False
                print(f'Congratulations, {name}') 
        else:
            print("entry only 'yes' or 'no'")
            continue

def main():
    get_a_number()


if __name__ == '__main__':
    main()
