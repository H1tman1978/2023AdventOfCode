import pytest
from Day1 import find_first_last_number  # Make sure to import the function from your script


# Test cases
@pytest.mark.parametrize("test_input,expected", [
    ("ninetwonine7ninetwonend", 91),
    ("oneight", 18),
    ("twone", 21),
    ("threeight", 38),
    ("sevenine", 79),
    ("one7three", 13),
    ("four9two", 42),
    # Add more test cases as needed
])
def test_find_first_last_number(test_input, expected):
    assert find_first_last_number(test_input) == expected
