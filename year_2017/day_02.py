import os

part_one_answer, part_two_answer = None, None


def main():
    solve()


def solve():
    global part_one_answer, part_two_answer
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split(sep="\n")
    words = words[:-1]
    part_one_answer = loop_over_input(words)
    print(f"part one answer: {part_one_answer}")

    # PART TWO
    part_two_answer = part_two_loop(words)
    print(f"part two answer: {part_two_answer}")


def loop_over_input(words):
    checksum_total = 0
    for i, word in enumerate(words):
        numbers = word.split(sep="\t")
        highest_so_far, lowest_so_far = int(numbers[0]), int(numbers[0])
        for number in numbers:
            number = int(number)
            if number > highest_so_far:
                highest_so_far = number
            elif number < lowest_so_far:
                lowest_so_far = number
        difference = highest_so_far - lowest_so_far
        checksum_total += difference
    return checksum_total


def part_two_loop(words):
    checksum_total = 0
    for word in words:
        numbers = word.split(sep="\t")
        checksum_total += find_only_even_division_result(numbers)
    return checksum_total


def find_only_even_division_result(numbers):
    for i, number in enumerate(numbers):
        number = int(number)
        for j, number2 in enumerate(numbers):
            number2 = int(number2)
            if i == j:
                continue
            if number % number2 == 0:
                return number // number2


if __name__ == "__main__":
    main()
