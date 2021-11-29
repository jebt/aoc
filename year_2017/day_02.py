import os


def main():
    solve()


def solve():
    with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
        puzzle_input = f.read()

    words = puzzle_input.split()
    print(words)
    loop_over_input(words)
    # print("part one placeholder")

    # PART TWO
    # print("part two placeholder")


def loop_over_input(words):
    for i, word in enumerate(words):
        print(i, word)


if __name__ == "__main__":
    main()
