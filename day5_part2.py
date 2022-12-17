def get_input_data():
    with open("day5_input") as day5_input:
        stacks_dict = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
        lines = []
        for line in day5_input:
            lines.append(line[0:-1])
        input_length = len(lines)
        n = 7
        while n >= 0:
            line = lines[n] + 33 * " "
            if line[1] != " ":
                stacks_dict[1] += line[1]
            if line[5] != " ":
                stacks_dict[2] += line[5]
            if line[9] != " ":
                stacks_dict[3] += line[9]
            if line[13] != " ":
                stacks_dict[4] += line[13]
            if line[17] != " ":
                stacks_dict[5] += line[17]
            if line[21] != " ":
                stacks_dict[6] += line[21]
            if line[25] != " ":
                stacks_dict[7] += line[25]
            if line[29] != " ":
                stacks_dict[8] += line[29]
            if line[33] != " ":
                stacks_dict[9] += line[33]
            n -= 1
        n = 10
        moves_instruction_list = []
        while 10 <= n < input_length:
            if lines[n][6] != ' ':
                crates_number = int(lines[n][5:7])
            else:
                crates_number = int(lines[n][5])
            source_stack = int(lines[n][-6])
            destination_stack = int(lines[n][-1])
            move_instruction = [crates_number, source_stack, destination_stack]
            moves_instruction_list.append(move_instruction)
            n += 1
    return stacks_dict, moves_instruction_list


def move(crates_number, source_stack, destination_stack, stacks_dict):
    if crates_number == 1:
        crate = stacks_dict[source_stack][-1]
        stacks_dict[source_stack] = stacks_dict[source_stack][:-1]
        stacks_dict[destination_stack] += crate
    else:
        crate = stacks_dict[source_stack][(-1 * crates_number):]
        stacks_dict[source_stack] = stacks_dict[source_stack][:(-1 * crates_number)]
        stacks_dict[destination_stack] += crate
    return stacks_dict


def get_moves_result(moves_instruction_list, stacks_dict):
    for one_move in moves_instruction_list:
        crates_number = one_move[0]
        source_stack = one_move[1]
        destination_stack = one_move[2]
        stacks_dict = move(crates_number, source_stack, destination_stack, stacks_dict)
    return stacks_dict

def get_elf_code():
    stacks_dict, moves_list = get_input_data()
    stack_dict = get_moves_result(moves_list, stacks_dict)
    end_state = stack_dict.values()
    elf_code = ''
    for state in end_state:
        elf_code += state[-1]
    return elf_code


print(get_elf_code())
