import string


def create_backpacks_list():
    with open("day3_input") as backpacks:
        backpacks_list = []
        for backpack in backpacks.readlines():
            backpacks_list.append(backpack[0:-1])
    return backpacks_list


def create_weight_dict():
    letters_list = string.ascii_letters
    weight_dict = dict()
    n = 1
    for letter in letters_list:
        weight_dict[letter] = n
        n += 1
    return weight_dict


def get_compartments(backpack):
    compartment_size = len(backpack)/2
    compartment1 = str()
    compartment2 = str()
    for letter in backpack:
        if len(compartment1) < compartment_size:
            compartment1 += letter
        else:
            compartment2 += letter
    return compartment1, compartment2


def compare_compartments(compartment1, compartment2):
    repeated_things = set()
    for letter in compartment1:
        if letter in compartment2:
            repeated_things.add(letter)
    return repeated_things


def count_weight(letter, weight_dict):
    letter_weight = weight_dict[letter]
    return letter_weight


def count_total_weight():
    weight_dict = create_weight_dict()
    backpacks_list = create_backpacks_list()
    total_weight = 0
    for backpack in backpacks_list:
        compartment1, compartment2 = get_compartments(backpack)
        print(compartment1)
        print(compartment2)
        repeated_things = compare_compartments(compartment1, compartment2)
        for thing in repeated_things:
            thing_weight = count_weight(thing, weight_dict)
            total_weight += thing_weight
            print(repeated_things)
            print(total_weight)
    return total_weight

total_weight = count_total_weight()
print(total_weight)

