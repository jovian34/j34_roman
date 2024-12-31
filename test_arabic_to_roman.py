import pytest
import arabic_to_roman


def test_value_map_points_to_correct_value():
    conversion = arabic_to_roman.ArabicToRoman()
    assert conversion.value_map[400] == "CD"


def test_convert_functions_throws_error_on_too_large_argument():
    conversion = arabic_to_roman.ArabicToRoman()
    with pytest.raises(ValueError) as excinfo:
        conversion.convert(4000)
    assert str(excinfo.value) == "This is not a valid integer for a Roman numeral"


def test_convert_functions_throws_error_on_too_small_argument():
    conversion = arabic_to_roman.ArabicToRoman()
    with pytest.raises(ValueError) as excinfo:
        conversion.convert(0)
    assert str(excinfo.value) == "This is not a valid integer for a Roman numeral"


def test_convert_functions_throws_error_on_non_integer():
    conversion = arabic_to_roman.ArabicToRoman()
    with pytest.raises(ValueError) as excinfo:
        conversion.convert(10.5)
    assert str(excinfo.value) == "This is not a valid integer for a Roman numeral"


def test_conversion_works_for_3999():
    conversion = arabic_to_roman.ArabicToRoman()
    assert conversion.convert(3999) == "MMMCMXCIX"


def test_conversion_works_for_3483():
    conversion = arabic_to_roman.ArabicToRoman()
    assert conversion.convert(3488) == "MMMCDLXXXVIII"


def test_conversion_works_for_1():
    conversion = arabic_to_roman.ArabicToRoman()
    assert conversion.convert(1) == "I"

