from enum import Enum
from operator import attrgetter


class Cube(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Lap:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def is_valid(self, bag_red, bag_green, bag_blue):
        return self.red <= bag_red and self.green <= bag_green and self.blue <= bag_blue


class Game:
    def __init__(self, game_id: int, laps: list):
        self.game_id = game_id
        self.laps = laps

    def is_valid(self, bag_red, bag_green, bag_blue):
        for lap in self.laps:
            if not lap.is_valid(bag_red, bag_green, bag_blue):
                return False
        return True

    def find_max_cube(self, cube: Cube):
        max_cube = min(self.laps, key=attrgetter(cube.value)).__getattribute__(cube.value)
        for lap in self.laps:
            lap_cube = lap.__getattribute__(cube.value)
            max_cube = max(max_cube, lap_cube)
        return max_cube

    def find_min_possible_lap(self):
        min_red_cube = self.find_max_cube(Cube.RED)
        min_green_cube = self.find_max_cube(Cube.GREEN)
        min_blue_cube = self.find_max_cube(Cube.BLUE)

        return Lap(min_red_cube, min_green_cube, min_blue_cube)


def get_lap(cubes: dict):
    red = 0
    green = 0
    blue = 0
    for cube, count in cubes.items():
        if Cube.RED == cube:
            red = int(count)
        elif Cube.BLUE == cube:
            blue = int(count)
        elif Cube.GREEN == cube:
            green = int(count)
    return Lap(red, green, blue)


def extract_laps(laps_str: str):
    laps = []
    for lap in laps_str.split(";"):
        cubes = {}
        for cube in lap.split(","):
            count_and_cube = cube.split(" ")
            cubes[Cube(count_and_cube[2])] = count_and_cube[1]
        laps.append(cubes)
    return laps


def extract_game(game_str: str):
    game_and_laps = game_str.split(":")
    laps = extract_laps(game_and_laps[1])
    laps_obj = []
    for lap in laps:
        laps_obj.append(get_lap(lap))
    return Game(int(game_and_laps[0].split(" ")[1]), laps_obj)


def sum_valid_games(games: [], bag_red, bag_green, bag_blue):
    game_id_sum = 0
    for game in games:
        if game.is_valid(bag_red, bag_green, bag_blue):
            game_id_sum += game.game_id
    return game_id_sum


def find_min_laps(games: list[Game]):
    min_laps = []
    for game in games:
        min_laps.append(game.find_min_possible_lap())

    return min_laps


def sum_min_laps(laps: list[Lap]):
    sum = 0
    for lap in laps:
        sum += lap.red * lap.blue * lap.green

    return sum


def read_input(filename):
    with open(filename) as file:
        return file.readlines()


input_text = read_input("day_2_input.txt")
games = []
for game_str in input_text:
    games.append(extract_game(game_str.removesuffix('\n')))
print(sum_valid_games(games, 12, 13, 14))
min_laps = find_min_laps(games)
print(f"sum of min possible laps: {sum_min_laps(min_laps)}")