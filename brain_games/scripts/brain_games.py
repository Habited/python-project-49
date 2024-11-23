#!/usr/bin/env python3
from brain_games.scripts.brain_even import game_parity_check
from brain_games.scripts.brain_calc import game_calc
from brain_games.scripts.brain_gcd import game_gcd
from brain_games.scripts.brain_progression import game_progression
from brain_games.scripts.brain_prime import game_prime


def main():
    game_parity_check()
    game_calc()
    game_gcd()
    game_progression()
    game_prime()


if __name__ == '__main__':
    main()
