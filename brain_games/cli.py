import prompt


def welcom_user():
    name: str = prompt.string("Welcome to the Brain Games!"
                              "May I have your name? ")
    print(f"Hello, {name}!")
