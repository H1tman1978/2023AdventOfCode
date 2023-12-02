import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def parse_game_data(line):
    """
    Parse a line of game data to extract the game ID and the counts of each color of cubes.

    Args:
    line (str): A string containing the game data.

    Returns:
    tuple: A tuple containing the game ID (int) and a list of dictionaries, each representing the cube counts for each color in a subset.
    """
    parts = line.split(': ')
    game_id = int(parts[0].split(' ')[1])  # Extracting the game ID
    cube_data = parts[1].split('; ')

    cube_counts = []
    for data in cube_data:
        counts = {'red': 0, 'green': 0, 'blue': 0}
        cubes = data.split(', ')
        for cube in cubes:
            count, color = cube.split(' ')
            color = color.strip()  # Remove any trailing whitespace or newline characters
            counts[color] = int(count)
        cube_counts.append(counts)

    logging.debug(f'Game {game_id} parsed with cube counts: {cube_counts}')
    return game_id, cube_counts


def is_game_possible(cube_counts, available_cubes):
    """
    Determine if a game is possible with the given cube counts and available cubes.

    Args:
    cube_counts (list): A list of dictionaries where each dictionary contains the cube counts for a subset.
    available_cubes (dict): A dictionary with the available cube counts for each color.

    Returns:
    bool: True if the game is possible, False otherwise.
    """
    for counts in cube_counts:
        if any(counts[color] > available_cubes[color] for color in counts):
            return False
    return True


def calculate_minimum_cubes(cube_counts):
    """
    Calculate the minimum number of cubes of each color needed to make the game possible.

    Args:
    cube_counts (list): A list of dictionaries where each dictionary contains the cube counts for a subset.

    Returns:
    dict: A dictionary with the minimum number of cubes required for each color.
    """
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for counts in cube_counts:
        for color in counts:
            min_cubes[color] = max(min_cubes[color], counts[color])
    return min_cubes


def calculate_power(cube_set):
    """
    Calculate the power of a set of cubes, defined as the product of the number of red, green, and blue cubes.

    Args:
    cube_set (dict): A dictionary with the count of cubes for each color.

    Returns:
    int: The calculated power of the set of cubes.
    """
    return cube_set['red'] * cube_set['green'] * cube_set['blue']


def main():
    """
    Main function to execute the puzzle solution. It reads game data, determines possible games and their
    minimum cube requirements, and calculates the total power.
    """

    # Read data from data file
    with open('data/day2_data.txt', 'r') as file:
        lines = file.readlines()

    # Part 1 Solution
    available_cubes = {'red': 12, 'green': 13, 'blue': 14}
    possible_game_ids = []
    for line in lines:
        game_id, cube_counts = parse_game_data(line)
        if is_game_possible(cube_counts, available_cubes):
            possible_game_ids.append(game_id)

    total = sum(possible_game_ids)
    print(f"The sum of the IDs of the possible games is: {total}")

    # Part 2 Solution
    total_power = 0
    for line in lines:
        game_id, cube_counts = parse_game_data(line)
        min_cubes = calculate_minimum_cubes(cube_counts)
        game_power = calculate_power(min_cubes)
        total_power += game_power
        print(f"Game {game_id}: Minimum cubes {min_cubes}, Power {game_power}")

    print(f"The sum of the power of the minimum sets is: {total_power}")


if __name__ == "__main__":
    main()
