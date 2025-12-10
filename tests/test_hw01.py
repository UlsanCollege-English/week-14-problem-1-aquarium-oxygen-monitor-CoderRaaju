import pathlib
import sys

import pytest

# Ensure hw01 directory is on the path so "from main import ..." works
THIS_FILE = pathlib.Path(__file__).resolve()
# Assuming main.py is in a directory one level up from the test file
HW_DIR = THIS_FILE.parents[1] 
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

# Import the function to be tested
from main import max_window_sum  # noqa: E402


@pytest.mark.parametrize(
    "readings,k,expected",
    [
        ([1, 2, 3, 4, 5], 2, 9),         # 4+5
        ([5, -1, 3, 2, 4], 3, 9),        # 5-1+3=7, -1+3+2=4, 3+2+4=9 (Corrected from user prompt comment, max is 9)
        ([10, 2, -5, 4, 3], 2, 12),      # 10+2=12
        ([0, 0, 0], 1, 0),               # Window [0], [0], [0]
        ([1, 1, 1, 1], 4, 4),            # Full length window
    ],
)
def test_basic_windows(readings, k, expected):
    """Tests basic functionality with various positive and mixed numbers."""
    assert max_window_sum(readings, k) == expected


def test_full_length_window():
    """Tests the case where k is the full length of the array."""
    readings = [3, 1, 2]
    assert max_window_sum(readings, 3) == sum(readings)


def test_negative_numbers_only():
    """Tests an array composed entirely of negative numbers."""
    readings = [-5, -2, -8, -1]
    # Window 2: [-5, -2] sum=-7; [-2, -8] sum=-10; [-8, -1] sum=-9
    assert max_window_sum(readings, 2) == -7
    # Window 3: [-5,-2,-8] sum=-15; [-2,-8,-1] sum=-11
    assert max_window_sum(readings, 3) == -11


@pytest.mark.parametrize("k", [0, -1, -5])
def test_invalid_k_non_positive(k):
    """Tests the ValueError case where k is 0 or negative."""
    with pytest.raises(ValueError):
        max_window_sum([1, 2, 3], k)


def test_invalid_k_too_large():
    """Tests the ValueError case where k is larger than the list length."""
    with pytest.raises(ValueError):
        max_window_sum([1, 2], 3)


def test_empty_readings_raises():
    """Tests the ValueError case where the readings list is empty."""
    with pytest.raises(ValueError):
        max_window_sum([], 1)


def test_larger_case_performance_like():
    """Tests a larger array to confirm correctness and implied O(N) performance."""
    readings = list(range(1, 501))  # 1..500
    k = 50
    # The maximum sum is the last 50 numbers: 451, 452, ..., 500
    expected = sum(readings[-k:])
    assert max_window_sum(readings, k) == expected