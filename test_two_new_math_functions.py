from two_new_math_functions import power, calculate_remainder

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9

def test_calculate_remainder():
    assert calculate_remainder(10, 3) == 1
    assert calculate_remainder(15, 5) == 0
    assert calculate_remainder(20, 7) == 6
