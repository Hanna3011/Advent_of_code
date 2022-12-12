def create_games_list():
    with open("day2_input") as games:
        games_list = []
        for game in games.readlines():
            games_list.append(game)
    return games_list


def get_value(choice):
    value_dict = {"rock": 1, "paper": 2, "scissors":3}
    choice_value = value_dict[choice]
    return choice_value

def get_choices(game):
    game_dict = {"Y": "paper", "X": "rock", "Z": "scissors",
                 "A": "rock", "B": "paper", "C": "scissors"}
    elf_choice = game_dict[game[0]]
    my_choice = game_dict[game[-2]]
    return elf_choice, my_choice


def if_win(my_choice, elf_choice):
    game_result = 0
    if elf_choice == my_choice:
        game_result = 0
    elif (elf_choice == "paper" and my_choice == "rock") \
            or (elf_choice == "scissors" and my_choice == "paper") \
            or (elf_choice == "rock" and my_choice == "scissors") :
        game_result = -1
    elif (my_choice== "paper" and elf_choice == "rock") \
         or (my_choice == "scissors" and elf_choice == "paper") \
         or (my_choice == "rock" and elf_choice == "scissors"):
        game_result = 1
    return game_result

def count_scores(game_result, choice_value):
    win_score = 0
    if game_result == 1:
        win_score = 6
    elif game_result == 0:
        win_score = 3
    else:
        win_score = 0
    score = win_score + choice_value
    return score

def calc_scores():
    game_list = create_games_list()
    total_score = 0
    for game in game_list:
        elf_choice, my_choice = get_choices(game)
        choice_value = get_value(my_choice)
        game_result = if_win(my_choice, elf_choice)
        score = count_scores(game_result,choice_value)
        total_score += score
    return total_score

print(calc_scores())




