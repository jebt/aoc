YEAR = 2017
DAY = 1


def puzzle_2017_1(puzzle_input):
    print(find_total(puzzle_input))

    # PART TWO
    steps_forward = (len(puzzle_input) - 1) // 2
    print(find_total(puzzle_input, steps=steps_forward))


def find_total(puzzle_input, steps=1):
    total = 0
    for i, digit in zip(range(len(puzzle_input)-1), puzzle_input):
        to_compare_index = (i + steps) % (len(puzzle_input) - 1)
        if digit == puzzle_input[to_compare_index]:
            total += int(digit)
    return total


def main():
    with open(f"{YEAR}/{DAY}/input.txt") as f:
        puzzle_input = f.read()
    puzzle_2017_1(puzzle_input)


if __name__ == "__main__":
    main()
