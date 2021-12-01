import os


part_one_answer, part_two_answer = None, None


def main():
    solve()


def solve():
    global part_one_answer, part_two_answer
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split()
    print(words)
    # numbers = [int(word) for word in words]
    # loop_over_input(words)

    part_one_answer = None
    print(f"part one answer: {part_one_answer}")

    # PART TWO
    part_two_answer = None
    print(f"part two answer: {part_two_answer}")


def loop_over_input(words):
    for i, word in enumerate(words):
        print(i, word)


if __name__ == "__main__":
    main()
