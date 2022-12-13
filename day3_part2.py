import string


def create_backpacks_list():
    with open("day3_input") as backpacks:
        backpacks_list = []
        for backpack in backpacks.readlines():
            backpacks_list.append(backpack[0:-1])
    return backpacks_list

def create_groups_lists(backpacks_list):
    groups_list = []
    group = []
    for backpack in backpacks_list:
        group.append(backpack)
        if len(group) == 3:
            groups_list.append(group)
            group = []
    return groups_list

def find_badges(group_list):
    all_badges = []
    for group in group_list:
        backpack1 = group[0]
        backpack2 = group[1]
        backpack3 = group[2]
        for thing in backpack1:
            if (thing in backpack2) and (thing in backpack3):
                badge = thing
        all_badges.append(badge)
    return all_badges


def count_weight(badge, weight_dict):
    badge_weight = weight_dict[badge]
    return badge_weight


def create_weight_dict():
    letters_list = string.ascii_letters
    weight_dict = dict()
    n = 1
    for letter in letters_list:
        weight_dict[letter] = n
        n += 1
    return weight_dict


def count_total_weight():
    weight_dict = create_weight_dict()
    backpacks_list = create_backpacks_list()
    group_list = create_groups_lists(backpacks_list)
    all_badges = find_badges(group_list)
    total_weight = 0
    for badge in all_badges:
        badge_weight = count_weight(badge, weight_dict)
        total_weight += badge_weight
    return total_weight

total_weight = print(count_total_weight())