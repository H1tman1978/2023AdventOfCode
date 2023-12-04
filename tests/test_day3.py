import pytest
from day_3 import calculate_gear_ratios, check_diagonal, check_vertical, is_symbol, get_all_adjacent_numbers, \
    sum_part_numbers, check_horizontal


def test_is_symbol():
    assert is_symbol('*') == True
    assert is_symbol('#') == True
    assert is_symbol('+') == True
    assert is_symbol('1') == False
    assert is_symbol('.') == False


def test_check_horizontal():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......"
    ]
    # Test position adjacent to '*' on row 2
    assert check_horizontal(schematic, 1, 3) == set()  # No numbers horizontally adjacent to '*'

    # Test position adjacent to '#' on row 4
    assert check_horizontal(schematic, 3, 6) == set()  # No numbers horizontally adjacent to '#'

    # Test position adjacent to '*' on row 5
    assert check_horizontal(schematic, 4, 3) == {7}  # Number '7' is to the left of '*'


def test_check_vertical():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......"
    ]
    # Test vertical position adjacent to '*' on row 2
    assert check_vertical(schematic, 1, 3) == {5}  # Number '5' is below '*'

    # Test vertical position adjacent to '#' on row 4
    assert check_vertical(schematic, 3, 6) == {6}  # Number '6' is above '#'

    # Test vertical position adjacent to '*' on row 5
    assert check_vertical(schematic, 4, 3) == set()  # No numbers are above or below '*'


def test_check_diagonal():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......"
    ]
    # Test diagonal position adjacent to '*' on row 2
    assert check_diagonal(schematic, 1, 3) == {3, 7}  # Numbers 3 and 7 are diagonally adjacent to '*'

    # Test diagonal position adjacent to '#' on row 4
    assert check_diagonal(schematic, 3, 6) == {3}  # Number '3' is diagonally adjacent to '#'

    # Test diagonal position adjacent to '*' on row 5
    assert check_diagonal(schematic, 4, 3) == set()  # No numbers are diagonally adjacent to '*'


def test_get_adjacent_numbers():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......"
    ]
    # Test different positions
    assert get_all_adjacent_numbers(schematic, 1, 3) == [467, 35]  # Adjacent to '*'
    assert get_all_adjacent_numbers(schematic, 3, 6) == [633]  # Adjacent to '#'
    assert get_all_adjacent_numbers(schematic, 4, 3) == [617]  # Adjacent to '*'


def test_sum_part_numbers():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
    assert sum_part_numbers(schematic) == 4361  # Example given in the problem


def test_calculate_gear_ratios():
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.."
    ]
    # In this schematic, there are two gears:
    # 1. The first gear is adjacent to 467 and 35, so its gear ratio is 16345.
    # 2. The second gear is adjacent to 755 and 598, so its gear ratio is 451490.
    # The sum of these gear ratios is 16345 + 451490 = 413537.
    assert calculate_gear_ratios(schematic) == 467835

