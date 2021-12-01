import os


part_one_answer, part_two_answer = None, None


def main():
    solve()


def solve():
    global part_one_answer, part_two_answer
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split()
    # numbers = [int(word) for word in words]

    part_one_answer, part_two_answer = loop_over_input(words)
    print(f"part one answer: {part_one_answer}")
    print(f"part two answer: {part_two_answer}")


def loop_over_input(words):
    answer1 = None
    answer2 = None
    for i, word in enumerate(words):
        print(i, word)
    return answer1, answer2


if __name__ == "__main__":
    main()
