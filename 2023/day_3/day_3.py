import re

special_characters = "!@#$%^&*()-+?_=,<>/"


class Schemantic:

    def __init__(self, schematic: str, top_schemantic: str, bottom_schemantic: str):
        self.schematic = schematic
        self.top_schemantic = top_schemantic
        self.bottom_schemantic = bottom_schemantic

    def find_next_part_number_index(self, start_index: int):
        match = re.search(r'\d', self.schematic[start_index:])
        if match is not None:
            return match.start()
        else:
            return -1

    def find_part_number_last_index(self, part_start_index):
        match = re.search(r'\D', self.schematic[part_start_index:])
        if match is not None:
            return match.start()
        else:
            return -1

    def contains_symbol(self, substring: str):
        return any(character in special_characters for character in substring)

    def symbol_exists_in_neighborhood(self, part_number_start_index, part_number_end_index):
        start_index = max(part_number_start_index - 1, 0)
        if self.contains_symbol(self.schematic[start_index]):
            return True

        end_index = min(part_number_end_index + 1, last_index - 1)
        if self.contains_symbol(self.schematic[end_index]):
            return True

        if self.contains_symbol(self.top_schemantic[start_index:end_index + 1]):
            return True

        if self.contains_symbol(self.bottom_schemantic[start_index:end_index + 1]):
            return True

        return False

    def check_schematic(self):
        parts_sum = 0
        cur_index = 0

        while cur_index < last_index:
            part_number_start_index = self.find_next_part_number_index(cur_index)

            if part_number_start_index >= 0:
                part_number_start_index += cur_index
                part_number_end_index = self.find_part_number_last_index(part_number_start_index)

                if part_number_end_index == -1:
                    part_number_end_index = last_index - 1
                else:
                    part_number_end_index = part_number_start_index + part_number_end_index - 1

                if self.symbol_exists_in_neighborhood(part_number_start_index, part_number_end_index):
                    parts_sum += int(self.schematic[part_number_start_index:part_number_end_index + 1])

                cur_index = part_number_end_index + 1
            else:
                cur_index = last_index

        return parts_sum


def build_schematics(engine_schematics: list[str]):
    schematics = []
    for index, schematic in enumerate(engine_schematics):
        top_schematic_index = index - 1
        top_schematic = ""
        if top_schematic_index >= 0:
            top_schematic = engine_schematics[top_schematic_index]
        else:
            top_schematic = "." * last_index
        bottom_schemantic_index = index + 1
        bottom_schematic = ""
        if bottom_schemantic_index < last_index:
            bottom_schematic = engine_schematics[bottom_schemantic_index]
        else:
            bottom_schematic = "." * last_index

        schematics.append(Schemantic(schematic, top_schematic, bottom_schematic))

    return schematics


def sum_part_numbers(schemantics: list[Schemantic]):
    total_parts_sum = 0
    for schemantic in schemantics:
        total_parts_sum += schemantic.check_schematic()

    return total_parts_sum


def clear_schemantincs(engine_schemantics: list[str]):
    clear_list = []

    for engine_schemantic in engine_schemantics:
        clear_list.append(engine_schemantic.rstrip())

    return clear_list


def read_input(filename):
    with open(filename) as file:
        return file.readlines()


engine_schematics = read_input("input.txt")
engine_schematics = clear_schemantincs(engine_schematics)
num_of_schematics = len(engine_schematics)
last_index = len(engine_schematics[0])
schemantics = build_schematics(engine_schematics)
print(f"Sum of all part numbers: {sum_part_numbers(schemantics)}")
