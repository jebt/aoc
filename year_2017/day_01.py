import os


part_one_answer, part_two_answer = None, None


def main():
    solve()


def solve():
    global part_one_answer, part_two_answer
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split()
    string = words[0]
    part_one_answer = find_total(string)
    print(f"part one answer: {part_one_answer}")

    # PART TWO
    steps_forward = len(string) // 2
    part_two_answer = find_total(string, steps=steps_forward)
    print(f"part two answer: {part_two_answer}")


def find_total(string, steps=1):
    total = 0
    for i, digit in enumerate(string):
        to_compare_index = (i + steps) % len(string)
        if digit == string[to_compare_index]:
            total += int(digit)
    return total


if __name__ == "__main__":
    main()
