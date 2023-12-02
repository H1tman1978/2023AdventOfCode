"""
day_1.py
Date: 12/01/23
Author: Tony Rolfe

Description:
This script is designed to solve a puzzle from the Advent of Code 2023 (https://adventofcode.com/2023/day/1).
It processes a file containing lines of text, each with a specific calibration value. The script identifies
and combines the first and last digits (or spelled-out numbers) on each line to form a single two-digit number.
The sum of all these two-digit numbers from the entire document provides the solution to the puzzle. It handles
both digits and spelled-out numbers ("one" through "nine") and is equipped to deal with various formatting
scenarios in the input data.

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
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

calibration_total = 0
file_path = 'data/day1_data.txt'  # Adjust the file path if necessary


def find_first_number(s, num_map):
    """Finds the first number in a string.

    Args:
        s (str): The string to search.
        num_map (dict): A dictionary mapping spelled-out numbers to digits.

    Returns:
        str: The first number found in the string as a digit. Returns None if no number is found.
    """
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for word, digit in num_map.items():
            if s.startswith(word, i):
                return digit
    return None


def find_last_number(s, num_map):
    """Finds the last number in a string.

    Args:
        s (str): The string to search, which will be reversed.
        num_map (dict): A dictionary mapping spelled-out numbers to digits.

    Returns:
        str: The last number found in the string as a digit. Returns None if no number is found.
    """
    s = s[::-1]
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for word, digit in num_map.items():
            if s.startswith(word, i):
                return digit
    return None


def find_first_last_number(s):
    """Finds both the first and last numbers in a string.

    Args:
        s (str): The string to search.

    Returns:
        int: The combined first and last numbers found in the string.

    Raises:
        ValueError: If less than two numbers are present in the string.
    """
    num_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    reversed_num_map = {word[::-1]: digit for word, digit in num_map.items()}

    first_number = find_first_number(s, num_map)
    last_number = find_last_number(s, reversed_num_map)

    if first_number is None or last_number is None:
        raise ValueError("The string must contain at least two numbers.")

    return int(first_number + last_number)


def main(total=0):
    """Processes lines from a file and calculates the total of first and last numbers found in each line.

    Args:
        total (int, optional): The initial total value. Defaults to 0.

    Returns:
        int: The cumulative total of first and last numbers found in each line of the file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                logging.info(f"Processing line: {stripped_line}")
                try:
                    number = find_first_last_number(stripped_line)
                    logging.info(f"Found number: {number}")
                    total += number
                    logging.info(f"Running total: {total}\n")
                except ValueError as e:
                    logging.error(f"Error processing line '{stripped_line}': {e}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    finally:
        return total


if __name__ == '__main__':
    calibration_total = main(calibration_total)
    print(calibration_total)
