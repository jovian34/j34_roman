def roman(letters):
    roman_values = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    subtract = {"C", "X", "I",}
    check_for_invalid_characters(letters, roman_values)
    check_for_too_many_repeated_letters(letters)
    return get_roman_value(letters, roman_values, subtract)

def check_for_invalid_characters(letters, roman_values):
    for letter in letters:
        if letter not in roman_values:
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

def get_roman_value(letters, roman_values, subtract):
    value = 0
    last = None
    for letter in letters:
        if last not in subtract or roman_values[last] >= roman_values[letter]:
            value += roman_values[letter]
        elif last == "I" and roman_values[letter] > 10:
            raise ValueError("This is not a valid Roman Numeral")
        elif last in subtract:
            value += roman_values[letter] - (2 * roman_values[last])
        last = letter
    if value > 0:
        return value
    else:
        raise ValueError("This is not a valid Roman Numeral")