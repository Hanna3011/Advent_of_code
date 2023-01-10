def read_information():
    with open("day7_input") as input_information:
        information_list = input_information.readlines()
    return information_list


def read_catalogs(information_list):
    catalogs = {}
    n_line = 0
    for command in information_list:
        if command != "$ cd ..\n":
            if "$ cd" in command:
                direction = "dir " + command[5:-1]
                contents = []
                for line in information_list[n_line+2:]:
                    if "$" not in line:
                        contents.append(line[:-1])
                    else:
                        break
                catalogs[direction] = contents
        n_line += 1
    return catalogs

def create_file_with_value_set(catalogs):
    file_with_value_set = set()
    for catalog in catalogs:
        potential_files = catalogs[catalog]
        for potential_file in potential_files:
            if "dir " not in potential_file:
                file_with_value_set.add(potential_file)
    return file_with_value_set

def create_dir_set(catalogs):
    dir_set = set()
    for catalog in catalogs:
        potential_dirs = catalogs[catalog]
        for potential_dir in potential_dirs:
            if "dir " in potential_dir:
                dir_set.add(potential_dir)
    return dir_set



# def create_value_dict(catalogs,file_with_value_set):
#     file_value_dict = {}
#     for file in file_with_value_set:
#         splited_file = file.split(" ")
#         file_name = splited_file[1]
#         file_value = int(splited_file[0])
#         file_value_dict[file_name] = file_value
#     return file_value_dict

def check_value(file_with_value):
    splited_file = file_with_value.split(" ")
    file_value = int(splited_file[0])
    return file_value

def count_content(catalogs, files_with_value_set, dir_value_dict):
    catalogs_values = {}
    for catalog in catalogs.keys():
        for item in catalogs[catalog]:
            if item in files_with_value_set:
                item_value = check_value(item)
                print(item_value)
                if catalog in catalogs_values.keys():
                    current_value = catalogs_values[catalog]
                    current_value += item_value
                    catalogs_values[catalog] = current_value
                else:
                    catalogs_values[catalog] = item_value
            elif item in dir_value_dict.keys():
                item_value = dir_value_dict[item]
                if catalog in catalogs_values.keys():
                    current_value = catalogs_values[catalog]
                    current_value += item_value
                    catalogs_values[catalog] = current_value
                else:
                    catalogs_values[catalog] = item_value
            print(catalogs_values)
    return catalogs_values

def check_if_counting_finished(catalog_values, catalogs):
    if_finished = True
    for catalog in catalogs.keys():
        if catalog not in catalog_values.keys():
            if_finished = False
    return if_finished

def create_dir_value_dict(catalogs_values):
    dir_value_dict = {}
    for catalog in catalogs_values.keys():
        if catalog_values[catalog] != 0:
            dir_value_dict[catalog] = catalog_values[catalog]
    return dir_value_dict



information_list = read_information()
catalogs = read_catalogs(information_list)
print(catalogs)
file_with_value_set = create_file_with_value_set(catalogs)
print(file_with_value_set)
finished = False
dir_value_dict = {}
while finished != True:
    catalog_values = count_content(catalogs, file_with_value_set, dir_value_dict)
    print("hey")
    dir_value_dict = create_dir_value_dict(catalog_values)
    print(dir_value_dict)
    finished = check_if_counting_finished(catalog_values, catalogs)
    # print(catalog_values)


