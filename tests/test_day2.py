import pytest
from day_2 import calculate_minimum_cubes, calculate_power, parse_game_data, is_game_possible


def test_parse_game_data():
    # Test case 1
    input_data = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    expected_output = (
        1,
        [{'blue': 3, 'red': 4, 'green': 0}, {'blue': 6, 'red': 1, 'green': 2}, {'blue': 0, 'red': 0, 'green': 2}]
    )
    assert parse_game_data(input_data) == expected_output

    # You can add more test cases with different input strings


def test_is_game_possible():
    available_cubes = {'red': 12, 'green': 13, 'blue': 14}

    # Test case where game is possible
    cube_counts = [{'blue': 3, 'red': 4, 'green': 2}, {'blue': 6, 'red': 1, 'green': 2}]
    assert is_game_possible(cube_counts, available_cubes) == True

    # Test case where game is impossible
    cube_counts = [{'blue': 15, 'red': 4, 'green': 2}]
    assert is_game_possible(cube_counts, available_cubes) == False

    # More test cases can be added to cover different scenarios


def test_calculate_minimum_cubes():
    # Test case 1
    cube_counts = [{'blue': 3, 'red': 4, 'green': 2}, {'blue': 6, 'red': 1, 'green': 2}]
    expected_min_cubes = {'red': 4, 'green': 2, 'blue': 6}
    assert calculate_minimum_cubes(cube_counts) == expected_min_cubes

    # Test case 2
    cube_counts = [{'blue': 1, 'red': 2, 'green': 3}, {'blue': 4, 'red': 2, 'green': 1}]
    expected_min_cubes = {'red': 2, 'green': 3, 'blue': 4}
    assert calculate_minimum_cubes(cube_counts) == expected_min_cubes

    # Add more test cases as needed


def test_calculate_power():
    # Test case 1
    cube_set = {'red': 4, 'green': 2, 'blue': 6}
    expected_power = 4 * 2 * 6
    assert calculate_power(cube_set) == expected_power

    # Test case 2
    cube_set = {'red': 2, 'green': 3, 'blue': 4}
    expected_power = 2 * 3 * 4
    assert calculate_power(cube_set) == expected_power
