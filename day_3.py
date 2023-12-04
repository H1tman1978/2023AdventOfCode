"""
day_3.py
Date: 12/03/23
Author: Tony Rolfe

Description:
This script is designed to solve a puzzle from the Advent of Code 2023 (https://adventofcode.com/2023/day/3).
The puzzle involves processing a schematic representation of an engine, where each line contains a mix of numbers
and symbols. The script identifies part numbers, which are numbers adjacent to symbols, and calculates the sum of
these part numbers for the puzzle's first part. In the second part, it identifies gears (denoted by '*' symbols
adjacent to exactly two numbers) and calculates their gear ratios by multiplying these numbers. The sum of all gear
ratios provides the solution to the second part of the puzzle. The script efficiently handles the identification
and processing of these elements within the schematic, ensuring accurate calculation of the required sums.

License:
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


def is_symbol(char):
    """Checks if a character is a symbol.

    Args:
        char (str): The character to check.

    Returns:
        bool: True if the character is not a digit or a period, False otherwise.
    """
    return not char.isdigit() and char != '.'


def check_horizontal(schematic, row, col):
    """Checks horizontally for numbers adjacent to a symbol at a given position.

    Args:
        schematic (list of str): The engine schematic.
        row (int): The row index of the symbol.
        col (int): The column index of the symbol.

    Returns:
        set: A set of adjacent numbers found horizontally.
    """
    adjacent_numbers = set()
    cols = len(schematic[0])
    for j in [col - 1, col + 1]:
        if 0 <= j < cols and schematic[row][j].isdigit():
            adjacent_numbers.add(int(schematic[row][j]))
    return adjacent_numbers


def check_vertical(schematic, row, col):
    """Checks vertically for numbers adjacent to a symbol at a given position.

    Args:
        schematic (list of str): The engine schematic.
        row (int): The row index of the symbol.
        col (int): The column index of the symbol.

    Returns:
        set: A set of adjacent numbers found vertically.
    """
    adjacent_numbers = set()
    rows = len(schematic)
    for i in [row - 1, row + 1]:
        if 0 <= i < rows and schematic[i][col].isdigit():
            adjacent_numbers.add(int(schematic[i][col]))
    return adjacent_numbers


def check_diagonal(schematic, row, col):
    """Checks diagonally for numbers adjacent to a symbol at a given position.

    Args:
        schematic (list of str): The engine schematic.
        row (int): The row index of the symbol.
        col (int): The column index of the symbol.

    Returns:
        set: A set of adjacent numbers found diagonally.
    """
    adjacent_numbers = set()
    rows, cols = len(schematic), len(schematic[0])
    diagonal_offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Offsets for diagonal positions

    for offset in diagonal_offsets:
        i, j = row + offset[0], col + offset[1]
        if 0 <= i < rows and 0 <= j < cols and schematic[i][j].isdigit():
            adjacent_numbers.add(int(schematic[i][j]))

    return adjacent_numbers


def extract_number(schematic, row, col):
    """Extracts a complete number (single or multi-digit) from a position in the schematic.

    Args:
        schematic (list of str): The engine schematic.
        row (int): The row index of the start of the number.
        col (int): The column index of the start of the number.

    Returns:
        tuple: A tuple containing the extracted number as an integer and the set of positions forming the number.
    """
    if not schematic[row][col].isdigit():
        return None, set()

    number = schematic[row][col]
    positions = {(row, col)}
    rows, cols = len(schematic), len(schematic[0])

    # Check horizontally (left and right)
    for j in range(col - 1, -1, -1):
        if schematic[row][j].isdigit():
            number = schematic[row][j] + number
            positions.add((row, j))
        else:
            break
    for j in range(col + 1, cols):
        if schematic[row][j].isdigit():
            number += schematic[row][j]
            positions.add((row, j))
        else:
            break

    # Check vertically (up and down)
    for i in range(row - 1, -1, -1):
        if schematic[i][col].isdigit():
            number = schematic[i][col] + number
            positions.add((i, col))
        else:
            break
    for i in range(row + 1, rows):
        if schematic[i][col].isdigit():
            number += schematic[i][col]
            positions.add((i, col))
        else:
            break

    return int(number), positions


def get_all_adjacent_numbers(schematic, row, col, checked_positions=None):
    """Gets all complete numbers adjacent to a given position.

    Args:
        schematic (list of str): The engine schematic.
        row (int): The row index of the position.
        col (int): The column index of the position.
        checked_positions (set, optional): Positions already checked. Defaults to None.

    Returns:
        list: A list of all adjacent numbers found.
    """
    if checked_positions is None:
        checked_positions = set()

    adjacent_numbers = []

    # Check horizontally, vertically, and diagonally
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (i, j) not in checked_positions and 0 <= i < len(schematic) and 0 <= j < len(schematic[0]):
                if (i != row or j != col) and schematic[i][j].isdigit():
                    number, positions = extract_number(schematic, i, j)
                    if number is not None:
                        adjacent_numbers.append(number)
                        checked_positions.update(positions)

    return adjacent_numbers


def sum_part_numbers(schematic):
    """Sums all part numbers in the schematic.

    Args:
        schematic (list of str): The engine schematic.

    Returns:
        int: The sum of all part numbers.
    """
    total_sum = 0
    for row in range(len(schematic)):
        for col in range(len(schematic[row])):
            if is_symbol(schematic[row][col]):
                total_sum += sum(get_all_adjacent_numbers(schematic, row, col))
    return total_sum


def calculate_gear_ratios(schematic):
    """Calculates the sum of gear ratios for all gears in the schematic.

    Args:
        schematic (list of str): The engine schematic.

    Returns:
        int: The sum of all gear ratios.
    """
    total_gear_ratio = 0
    rows, cols = len(schematic), len(schematic[0])

    for row in range(rows):
        for col in range(cols):
            if schematic[row][col] == '*':
                # Get numbers adjacent to the gear
                adjacent_numbers = get_all_adjacent_numbers(schematic, row, col, set())
                if len(adjacent_numbers) == 2:
                    # This is a gear, calculate its gear ratio
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    total_gear_ratio += gear_ratio

    return total_gear_ratio


def main():
    """Main function to execute the puzzle solutions."""

    # Read data from file
    with open('data/day3_data.txt', 'r') as file:
        schematic = [line.strip() for line in file]

    # Part 1 Solution
    total = sum_part_numbers(schematic)
    print(f"The sum of all part numbers in the engine schematic is: {total}")

    # Part 2 Solution
    total_gear_ratio = calculate_gear_ratios(schematic)
    print(f"The sum of all gear ratios in the engine schematic is: {total_gear_ratio}")


if __name__ == "__main__":
    main()
