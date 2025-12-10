import pathlib
import sys

import pytest

# Ensure hw01 directory is on the path so "from main import ..." works
THIS_FILE = pathlib.Path(__file__).resolve()
HW_DIR = THIS_FILE.parents[1]
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

from main import max_window_sum  # noqa: E402


@pytest.mark.parametrize(
    "readings,k,expected",
    [
        ([1, 2, 3, 4, 5], 2, 9),          # 4+5
        ([5, -1, 3, 2, 4], 3, 9),         # 5-1+3=7, -1+3+2=4, 3+2+4=9
        ([10, 2, -5, 4, 3], 2, 12),        # 10+2=12
        ([0, 0, 0], 1, 0),
    ],
)
def test_basic_windows(readings, k, expected):
    assert max_window_sum(readings, k) == expected


def test_full_length_window():
    readings = [3, 1, 2]
    assert max_window_sum(readings, 3) == sum(readings)


def test_negative_numbers_only():
    readings = [-5, -2, -8, -1]
    # best window of size 2 is -7 (-5 + -2)
    assert max_window_sum(readings, 2) == -7


@pytest.mark.parametrize("k", [0, -1, -5])
def test_invalid_k_non_positive(k):
    with pytest.raises(ValueError):
        max_window_sum([1, 2, 3], k)


def test_invalid_k_too_large():
    with pytest.raises(ValueError):
        max_window_sum([1, 2], 3)


def test_empty_readings_raises():
    with pytest.raises(ValueError):
        max_window_sum([], 1)


def test_larger_case_performance_like():
    readings = list(range(1, 501))  # 1..500
    k = 50
    # The maximum sum is the last 50 numbers
    expected = sum(range(451, 501))
    assert max_window_sum(readings, k) == expected