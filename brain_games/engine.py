import prompt


def run_games(instruction, number_of_rounds,
              get_answer_and_question):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')

    print(f'Hello, {name}!\n'
          f'{instruction}')

    for _ in range(number_of_rounds):
        correct_answer, question = get_answer_and_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"'Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
