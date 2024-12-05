from random import choice, randint


def get_random_num() -> int:
    return randint(1, 100)


def get_random_symbol(list_symbol) -> str:
    return choice(list_symbol)
