def get_assignments_list():
    with open("day4_input") as assignments:
        assignments_list = []
        for assignment in assignments:
            assignments_list.append(assignment[0:-1])
    return assignments_list



def create_areas_list(assignments_list):
    areas_list = []
    for list in assignments_list:
        areas_list.append(list.replace("-",",").split(","))
    return areas_list

def get_elfs_all_area(areas_list):
    first_elf_start = int(areas_list[0])
    first_elf_end = int(areas_list[1])
    second_elf_start = int(areas_list[2])
    second_elf_end = int(areas_list[3])
    if first_elf_start == first_elf_end:
        first_elf_list = [first_elf_start]
    else:
        first_elf_list = list(range(first_elf_start, first_elf_end+1))
    if second_elf_start == second_elf_end:
        second_elf_list = [second_elf_start]
    else:
        second_elf_list = list(range(second_elf_start, second_elf_end+1))
    return first_elf_list, second_elf_list

def if_repeat(first_elf_list, second_elf_list):
    for area in first_elf_list:
        if area in second_elf_list:
            repeat = True
        else:
            repeat = False
            break
    if repeat == True:
        return repeat
    else:
        for area in second_elf_list:
            if area in first_elf_list:
                repeat = True
            else:
                repeat = False
                break
        return repeat


def count_repeats():
    assignments_list = get_assignments_list()
    areas_list = create_areas_list(assignments_list)
    repeat_sum = 0
    for area in areas_list:
        first_elf_areas, second_elf_areas = get_elfs_all_area(area)
        repeat = if_repeat(first_elf_areas, second_elf_areas)
        if repeat == True:
            repeat_sum += 1
    return repeat_sum


print(count_repeats())

