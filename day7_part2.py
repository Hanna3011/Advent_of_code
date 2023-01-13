def read_information():
    with open("day7_input") as input_information:
        input_list_with_enter = input_information.readlines()  # tworzenie listy kompletnych linii razem z znakami nowego wiersza
        input_list = []
        for element in input_list_with_enter:
            input_list.append(element[:-1])  # tworzenie listy kolejnych linii bez znaku /n
    return input_list


def create_content_path_dicts(
        input_list):  # fukcja zwraca 2 słowniki, każdy folder zawiera swój numer, w jednym słowniku numer zawiera wartość ścieżki folderu w postaci kolejnych nadfolderów na liście, a w drugim wartością jest lista zawartości
    path = []
    content = []
    n_line = 0  # numer linii (pozycji na liście z wejściowymi danymi)
    folder_content_dict = {}
    path_number = 1  # nadawanie numeru ścieżce jako klucza do słowników
    path_number_dict = {}
    for line in input_list:
        if line[0:4] == "$ cd":  # sprawdzam, czy dana linia mówi o zmianie lokalizacji
            if line[
               5:] == "..":  # jeśli linia cofa nas o folder do tyłu, odejmuję ze ścieżki ostatni element, czyli nazwę folderu, który opuszczam
                del path[-1]
            else:  # jeśli linia oznacza wejście do folderu, dodaję do ścieżki nazwę folderu, do którego wchodzę
                path.append(line[5:])
        elif line[
             0:4] == "$ ls":  # przy natknięciu się na tę komendę, dla aktualnej ścieżki w kolejnych liniach wyświetli się zawartość
            for line_after_ls in input_list[
                                 n_line + 1:]:  # iteruję po kolejnych liniach po $ ls dopóki nie natknę się na komendę cd lub ls
                if line_after_ls[
                   0:4] == "$ cd":  # jeśli napotkam komendę cd, oznacza to, że uzupełniana lista zawartości folderu jest kompletna (zakończyło się wymienianie elementów)
                    path_number_dict[
                        path_number] = path.copy()  # kopiuję zawartość ścieżki jako wartość dla numeru ścieżki do słownika path_number_dict
                    folder_content_dict[
                        path_number] = content.copy()  # analogicznie jak wyżej wypełniam drugi słownik - dla numeru ścieżki przypisuję wartość zawartości jako listy
                    path_number += 1  # ponieważ kończę akcję dla tej ścieżki, zakładam numer zwiększony o jeden dla kolejnej
                    content = []  # zeruję listę dla zawartości
                    break
                else:
                    content.append(
                        line_after_ls)  # kolejne wymienione elementy dokładam do zawartości folderu o danej liczbie
        n_line += 1  # zwiększam numer linii dla kolejnej analizowanej
    path_number_dict[path_number] = path.copy()
    folder_content_dict[path_number] = content.copy()
    return folder_content_dict, path_number_dict


def find_max_path_len(
        path_number_dict):  # ponieważ analizę zawartości będę wykonywać od najbardziej wewnętrznego folderu, szukam najdłuższej możliwej ścieżki
    lenths = []
    for number in path_number_dict.keys():  # dla każdego numeru ścieżki analizuję długość jej ścieżki
        lenths.append(len(path_number_dict[number]))
    max_lenth = max(lenths)  # wybieram najdłuższą ze wszystkich ścieżek
    return max_lenth


def rename_dir_to_path(folder_content_dict,
                       path_number_dict):  # aby dobrze korzystać ze słowników, w zawartości zamiast nazwy w formacie "dir xyz" wstawiam ścieżkę zakończoną nazwą folderu xyz
    for number in folder_content_dict.keys():
        path_number = number
        path = path_number_dict[path_number]
        for element in folder_content_dict[number]:
            index = folder_content_dict[number].index(
                element)  # tworzę zmienną z pozycją danego elementu na liście zawartości, bym mogła potem go podmienić
            if element[
               0:4] == "dir ":  # jeśli element zawiera pocztątek dir, to znaczy że jest folderem i chcę zamienić go na ścieżkę
                new_name = path.copy()  # kopiuję aktualną ścieżkę jako nową nazwę
                new_name.append(element[4:])  # do nowej nazwy dodaję nazwę folderu (z pominięciem "dir"
                folder_content_dict[number][
                    index] = new_name  # do listy z zawartością w miejsce starego "dir xyz" wklejam ścieżkę
    return folder_content_dict


def create_value_dict(folder_content_dict,
                      path_number_dict):  # funkcja służy do stworzenia słownika, który będzie zawierał informacje o numerze folderu oraz wielkości jego zawartości
    value_dict = {}
    longest_path = find_max_path_len(path_number_dict)
    for length in reversed(
            range(longest_path + 1)):  # wykonuję polecenie dla wszystkich zawartości po kolei, rozpoczynając od folderów z najdłuższą ścieżką, kończąc na najmniejszej
        for number in folder_content_dict.keys():
            if len(path_number_dict[
                       number]) == length:  # sprawdzam, czy moja ścieżka jest równa co do długości aktualnie analizowanym
                # path = path_number_dict[number]
                folder_value = 0  # wejściowym "rozmiarem" folderu jest 0
                for content in folder_content_dict[number]:  # analizuję zawartość folderu
                    if type(content) == str:  # jeśli dany element jest plikiem, czyli stringiem, bo foldery będą już listami
                        splited_file = content.split(" ")  # dzielę element na nazwę i rozmiar
                        file_name = splited_file[1]
                        file_value = int(splited_file[0])
                        folder_value += file_value  # zawartość folderu zwiększa się o zawartość pliku
                    else:  # jeśli element nie jest stringiem, tylko ścieżką, to muszę odczytać rozmiar całego folderu ze słownika
                        paths_list = list(
                            path_number_dict.values())  # tworzę listę ze wszystkimi ścieżkami i szukam pozycji mojej ścieżki
                        number_content = paths_list.index(
                            content) + 1  # odczytuję numer przypisany ścieżce, którą reprezentuje mój content
                        dir_value = value_dict[number_content]  # rozmiar folderu odczytuję ze słownika
                        folder_value += dir_value
                value_dict[number] = folder_value  # dany numer folderu otrzymuje wartość
    return value_dict


def find_smallest_dir_to_remove():
    information_list = read_information()
    folder_content_dict, path_number_dict = create_content_path_dicts(information_list)
    rename_dir_to_path(folder_content_dict, path_number_dict)
    value_dict = create_value_dict(folder_content_dict, path_number_dict)
    print(path_number_dict)
    sum_all_contents = value_dict[1]
    print(sum_all_contents)
    amount_to_remove = 30000000 - (70000000 - sum_all_contents)
    dir_values = list(value_dict.values())
    potential_dirs_to_remove = []
    for number in value_dict.keys():
        if value_dict[number] >= amount_to_remove:
            potential_dirs_to_remove.append((value_dict[number]))
    smallest_value_to_remove = min(potential_dirs_to_remove)
    return smallest_value_to_remove



print(find_smallest_dir_to_remove())