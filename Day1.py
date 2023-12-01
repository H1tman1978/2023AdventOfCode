import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

calibration_total = 0
file_path = 'day1_data.txt'  # Adjust the file path if necessary


def find_first_number(s, num_map):
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for word, digit in num_map.items():
            if s.startswith(word, i):
                return digit
    return None


def find_last_number(s, num_map):
    s = s[::-1]
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for word, digit in num_map.items():
            if s.startswith(word, i):
                return digit
    return None


def find_first_last_number(s):
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
