import re


def find_common_numbers(card: str):
    semicolon_index = card.find(':')
    seperator_index = card.find('|')
    winning_numbers = re.findall(r'\d+', card[semicolon_index:seperator_index])
    having_numbers = re.findall(r'\d+', card[seperator_index:])
    numbers_intersection = (list(set(winning_numbers) & set(having_numbers)))
    return numbers_intersection


def calculate_card_points(card: str):
    common_numbers = find_common_numbers(card)

    card_points_sum = 0
    if common_numbers:
        card_points_sum = 1

    card_points_sum *= pow(2, max(len(common_numbers) - 1, 0))

    return card_points_sum


def calculate_points(cards: list[str]):
    points_sum = 0
    for card in cards:
        points_sum += calculate_card_points(card)

    return points_sum


def construct_map(cards_count: int):
    card_copies = {}

    for i in range(cards_count):
        card_copies[i] = 1

    return card_copies


def calculate_copies(cur_card_index: int, number_of_matches: int):
    for i in range(number_of_matches):
        copy_index = cur_card_index + i + 1
        card_copies[copy_index] += card_copies[cur_card_index]


def calculate_scratchcards(cards: list[str]):
    for index in range(len(cards)):
        number_of_common_numbers = len(find_common_numbers(cards[index]))
        calculate_copies(index, number_of_common_numbers)


def read_input(filename):
    with open(filename) as file:
        return file.readlines()


scratchcards = read_input("day_4_input.txt")
print(f"points: {calculate_points(scratchcards)}")

# part 2
number_of_cards = len(scratchcards)
card_copies = construct_map(number_of_cards)
calculate_scratchcards(scratchcards)
print(f"sum of cards: {sum(card_copies.values())}")
