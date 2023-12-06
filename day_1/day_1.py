import re

digit_from_word = {
    "oneight": "18",
    "twone": "21",
    "threeight": "38",
    "fiveight": "58",
    "sevenine": "79",
    "eightwo": "82",
    "eighthree": "83",
    "nineight": "89",


    # "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def convert_words_to_digit(text):
    for word, digit in digit_from_word.items():
        text = str(text).replace(word, digit)

    return text


def calculate_calibration_value(text):
    text = convert_words_to_digit(text)
    values = re.findall(r'\d', text)
    return values[0] + values[-1]


def read_input(filename):
    with open(filename) as file:
        return file.readlines()


def sum_calibrations(texts):
    calibration_sum = 0
    for text in texts:
        calibration_sum += int(calculate_calibration_value(text))

    return calibration_sum


input_text = read_input("day1_input.txt")
print(sum_calibrations(input_text))
