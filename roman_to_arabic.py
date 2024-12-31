import arabic_to_roman


def roman(letters):
    convert = arabic_to_roman.ArabicToRoman()
    convert.make_reverse_map()
    try:
        return convert.reverse_map[letters]
    except KeyError:
        raise ValueError("This is not a valid Roman Numeral")