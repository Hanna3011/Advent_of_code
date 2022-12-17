def get_full_signal():
    with open("day6_input") as full_input_signal:
        full_signal = full_input_signal.readline()
        full_signal = full_signal[:-1]
    return full_signal

def find_first_marker(full_signal):
    n = 4
    for letter in full_signal[3:]:
        letters = set()
        letters.add(letter)
        letters.add(full_signal[n-2])
        letters.add(full_signal[n-3])
        letters.add(full_signal[n-4])
        if len(letters) == 4:
            print(letters)
            return n
        else:
            n += 1

full_signal = get_full_signal()
print(full_signal)
# print(find_first_marker(full_signal))