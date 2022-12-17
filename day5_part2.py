def get_input_data():
    with open("day5_input") as day5_input:
        stack_dict = {1 : "", 2 : "", 3 : "", 4 : "", 5 : "", 6 : "", 7 : "", 8 : "", 9: ""}
        lines = []
        input_lenght = len(lines)
        for line in day5_input:
            lines.append(line[0:-1])
        input_lenght = len(lines)
        n = 7
        while n >= 0:
            line = lines[n] + 33 * " "
            if line[1] != " ":
                stack_dict[1] += line[1]
            if line[5] != " ":
                stack_dict[2] += line[5]
            if line[9] != " ":
                stack_dict[3] += line[9]
            if line[13] != " ":
                stack_dict[4] += line[13]
            if line[17] != " ":
                stack_dict[5] += line[17]
            if line[21] != " ":
                stack_dict[6] += line[21]
            if line[25] != " ":
                stack_dict[7] += line[25]
            if line[29] != " ":
                stack_dict[8] += line[29]
            if line[33] != " ":
                stack_dict[9] += line[33]
            n -= 1
        n = 10
        moves_list = []
        while n >= 10 and n < input_lenght:
            if lines[n][6] != ' ':
                crates_number = int(lines[n][5:7])
            else:
                crates_number = int(lines[n][5])
            source_stack = int(lines[n][-6])
            destination_stack = int(lines[n][-1])
            move = [crates_number,source_stack,destination_stack]
            moves_list.append(move)
            n += 1
    return stack_dict, moves_list

def move(crates_number, source_stack, destination_stack, stack_dict):
    if crates_number == 1:
        crate = stack_dict[source_stack][-1]
        stack_dict[source_stack] = stack_dict[source_stack][:-1]
        stack_dict[destination_stack] += crate
    else:
        crate = stack_dict[source_stack][(-1 * crates_number):]
        stack_dict[source_stack] = stack_dict[source_stack][:(-1 * crates_number)]
        stack_dict[destination_stack] += crate
    print(crate)
    print(stack_dict)
    return stack_dict


def get_moves_result(moves_list,stack_dict):
    for one_move in moves_list:
        crates_number = one_move[0]
        source_stack = one_move[1]
        destination_stack = one_move[2]
        stack_dict = move(crates_number,source_stack,destination_stack,stack_dict)
        print(stack_dict)
    return stack_dict

stack_dict, moves_list = get_input_data()
print(stack_dict)
print(moves_list)
stack_dict = get_moves_result(moves_list,stack_dict)
end_state = stack_dict.values()
elf_code = ''
for state in end_state:
    elf_code += state[-1]
print(elf_code)

