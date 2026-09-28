import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from ohms_law import (
    calculate_current,
    calculate_voltage,
    calculate_resistance
)


def test_current():
    assert calculate_current(12, 6) == 2


def test_voltage():
    assert calculate_voltage(2, 6) == 12


def test_resistance():
    assert calculate_resistance(12, 2) == 6


def test_zero_resistance():
    try:
        calculate_current(12, 0)
        assert False
    except ValueError:
        assert True


print("All Ohm's Law test cases passed!")