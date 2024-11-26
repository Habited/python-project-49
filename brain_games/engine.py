import prompt


def run_games(list_of_question, number_of_rounds,
              get_answer_and_player_responce):
    print("Welcome to the Brain Games!")
    name: str = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(list_of_question)

    for _ in range(number_of_rounds):
        correct_answer, player_responce = get_answer_and_player_responce()
        if correct_answer == player_responce:
            print('Correct!')
        else:
            print(f"'{player_responce}' is wrong answer ;(."
                  f"'Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}')
