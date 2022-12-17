def get_full_signal():
    with open("day6_input") as full_input_signal:
        full_signal = full_input_signal.readline()
        full_signal = full_signal[:-1]
    return full_signal

def find_start_of_message(full_signal):
    n = 14
    for letter in full_signal[13:]:
        letters = set()
        letters.add(letter)
        for number in range(n-14, n-1):
            letters.add(full_signal[number])
        if len(letters) == 14:
            return n
        else:
            n += 1

full_signal = get_full_signal()
print(find_start_of_message(full_signal))
