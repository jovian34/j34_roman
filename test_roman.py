import pytest
from roman import roman

def test_function_exists():
    assert roman


def test_roman_takes_argument():
    assert roman("MMM")


def test_roman_takes_mmm_returns_3000():
    assert roman("MMM") == 3000


def test_roman_takes_m_returns_1000():
    assert roman("M") == 1000


def test_roman_takes_d_returns_500():
    assert roman("D") == 500


def test_roman_takes_md_returns_1500():
    assert roman("MD") == 1500


def test_roman_takes_c_returns_100():
    assert roman("C") == 100


def test_roman_takes_cm_returns_900():
    assert roman("CM") == 900


def test_roman_takes_cd_returns_400():
    assert roman("CD") == 400


def test_roman_takes_cdl_returns_450():
    assert roman("CDL") == 450


def test_roman_takes_x_returns_10():
    assert roman("X") == 10


def test_roman_takes_xx_returns_20():
    assert roman("XX") == 20


def test_roman_takes_xm_returns_990():
    assert roman("XM") == 990


def test_roman_takes_cmx_returns_910():
    assert roman("CMX") == 910


def test_roman_takes_mmmcmxc_returns_3990():
    assert roman("MMMCMXC") == 3990


def test_roman_takes_mmmcmlxxx_returns_3980():
    assert roman("MMMCMLXXX") == 3980


def test_roman_takes_v_returns_5():
    assert roman("V") == 5


def test_roman_takes_mmmcmxcv_returns_3995():
    assert roman("MMMCMXCV") == 3995


def test_roman_takes_i_returns_1():
    assert roman("I") == 1


def test_roman_takes_iii_returns_3():
    assert roman("III") == 3


def test_roman_takes_mmmcmxcviii_returns_3998():
    assert roman("MMMCMXCVIII") == 3998


def test_roman_takes_ix_returns_9():
    assert roman("IX") == 9


def test_roman_takes_mmmcmxcix_returns_3999():
    assert roman("MMMCMXCIX") == 3999


def test_ten_roman_numerals_from_random_generator():
    assert roman("DCXVIII") == 618
    assert roman("XXVIII") == 28
    assert roman("DCCLXXXIX") == 789
    assert roman("CMXCIII") == 993
    assert roman("DXIII") == 513
    assert roman("DCCCXII") == 812
    assert roman("DXXXV") == 535
    assert roman("CMV") == 905
    assert roman("CDVIII") == 408
    assert roman("DXLVIII") == 548