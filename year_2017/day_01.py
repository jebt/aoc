import os


def main():
    solve()


def solve():
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split()
    string = words[0]
    print(find_total(string))

    # PART TWO
    steps_forward = len(string) // 2
    print(find_total(string, steps=steps_forward))


def find_total(string, steps=1):
    total = 0
    for i, digit in enumerate(string):
        to_compare_index = (i + steps) % len(string)
        if digit == string[to_compare_index]:
            total += int(digit)
    return total


if __name__ == "__main__":
    main()
