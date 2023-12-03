# Day 1, puzzle 1

def get_calibration_value(input_line):
    for character in input_line:
        if is_integer(character):
            calibration_value = character
            break

    for character in input_line[::-1]:
        if is_integer(character):
            calibration_value += character
            break

    return int(calibration_value)


def is_integer(character):
    try:
        int(character)
        return True
    except ValueError:
        return False


def get_input_lines():
    input_lines = []
    with open("./day_01/01_input.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            input_lines.append(line)
    return input_lines


def test_calibration():
    source_strings = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    expected_calibration_values = [12, 38, 15, 77]

    calculated_calibration_values = []
    for input_string in source_strings:
        calib_value = get_calibration_value(input_string)
        calculated_calibration_values.append(calib_value)

    assert sum(expected_calibration_values) == sum(calculated_calibration_values), \
        f"Calculated calibration values dont match expected calibration values {calculated_calibration_values} != {expected_calibration_values}"    # noqa: E501
    print("+++++++++++++++\nTest successful\n+++++++++++++++")


def main():
    test_calibration()
    input_lines = get_input_lines()
    calibration_values = [get_calibration_value(input_line) for input_line in input_lines]  # noqa: E501
    checksum = sum(calibration_values)
    print(f"The sum of all calibration values is: {checksum}")


if __name__ == "__main__":
    main()
