from random import randint, choice


def get_random_num() -> int:
    return randint(1, 100)


def get_random_symbol(list_symbol) -> str:
    return choice(list_symbol)
