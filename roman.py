roman_value_map = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}
subtract = ["C", "X", "I",]

roman_values = [ value for key, value in roman_value_map.items() ]


def roman(letters):
    check_for_invalid_characters(letters, roman_value_map)
    check_for_too_many_repeated_letters(letters)
    return check_for_invalid_order(letters)

def check_for_invalid_characters(letters, roman_value_map):
    for letter in letters:
        if letter not in roman_value_map:
            raise ValueError("This is not a valid Roman Numeral")
        
def check_for_too_many_repeated_letters(letters):
    if letter_repeated_more_than_three_times(letters):
        raise ValueError("This is not a valid Roman Numeral")

def letter_repeated_more_than_three_times(letters):
    repeat = 0
    last = None
    for letter in letters:
        if last == letter:
            repeat += 1
        else:
            repeat = 0
            last = letter
        if repeat == 3:
            return True
    return False

def check_for_invalid_order(letters):
    letter_order = { order: [letter, roman_value_map[letter]] for order, letter in enumerate(letters) }
    keys_to_delete = []
    for key, values in letter_order.items():
        if key == len(letter_order)-1:
            pass
        elif values[0] in subtract:
            if values[1] < letter_order[key+1][1]:
                letter_order[key] = [
                    f"{letter_order[key][0]}{letter_order[key+1][0]}",
                    letter_order[key+1][1] - letter_order[key][1]
                ]
                keys_to_delete.append(key+1)
            if values[0] == "I" and letter_order[key+1][1] > 10:
                raise ValueError("This is not a valid Roman Numeral")
    for key in keys_to_delete:
        del letter_order[key]
    last_value = 0
    value = 0
    for order, values in letter_order.items():
        if last_value == 0:
            last_value = values[1]
            value = values[1]
        elif last_value <= values[1] and values[1] not in roman_values:
            raise ValueError("This is not a valid Roman Numeral")
        else:
            last_value = values[1]
            value += values[1]
    if value > 0:
        return value
    else:
        raise ValueError("This is not a valid Roman Numeral")
