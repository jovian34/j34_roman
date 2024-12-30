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
    subtract = ["C", "X", "I",]
    return get_roman_value(letters, roman_values, subtract)


def get_roman_value(letters, roman_values, subtract):
    value = 0
    last = None
    for letter in letters:
        if last not in subtract or roman_values[last] >= roman_values[letter]:
            value += roman_values[letter]
        else:
            value += roman_values[letter] - (2 * roman_values[last])
        last = letter
    return value