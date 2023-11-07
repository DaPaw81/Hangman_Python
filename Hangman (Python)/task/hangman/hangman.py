import random

wl_ratio = {'win': 0, 'lose': 0}


def uncover_letter(chosen_word, hint, user_input):
    return ''.join([user_input if chosen_word[i] == user_input else hint[i] for i in range(len(chosen_word))])


def update_attempts_and_choices(user_input, choices, chosen_word, attempts):
    if user_input in choices:
        print("You've already guessed this letter.")
        return attempts
    else:
        choices[user_input] = 1
        if user_input not in chosen_word:
            print("That letter doesn't appear in the word.")
            return attempts - 1
    return attempts


def print_results():
    print(f"You won: {wl_ratio['win']} times")
    print(f"You lost: {wl_ratio['lose']} times")


def game(chosen_word, hint, choices, attempts):
    while attempts > 0 and '-' in hint:
        print('\n' + hint)
        user_input = input("Input a letter: ")

        if len(user_input) != 1 or user_input == "":
            print("Please, input a single letter.")
            continue
        if not user_input.islower() or not user_input.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        attempts = update_attempts_and_choices(user_input, choices, chosen_word, attempts)
        hint = uncover_letter(chosen_word, hint, user_input)

    if '-' not in hint:
        print("\nYou guessed the word", chosen_word + '!')
        print("You survived!")
        wl_ratio['win'] += 1
    else:
        print("\nYou lost!")
        wl_ratio['lose'] += 1


def menu():
    while True:
        menu_choice = input('Type "play" to play the game, '
                            '"results" to show the scoreboard, and "exit" to quit: ').lower()
        if menu_choice == 'play':
            words = ['python', 'java', 'swift', 'javascript']
            chosen_word = random.choice(words)
            hint = '-' * len(chosen_word)
            attempts = 8
            choices = {}
            game(chosen_word, hint, choices, attempts)
        elif menu_choice == 'results':
            print_results()
        elif menu_choice == 'exit':
            break
        else:
            continue


print('H A N G M A N')
menu()
