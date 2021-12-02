import year_2021.day_03 as day

from os.path import splitext


# todo: add sample input test with assert answer == sample answer
# todo: command line args: year, day, all, default to today, else last available, use_sample
# todo: dynamic import strings only the days needed for execution
#  see: https://stackoverflow.com/questions/301134/how-to-import-a-module-given-its-name-as-string


def main():
    with open(f"{splitext(day.__file__)[0]}_input.txt") as file:
        puzzle_input = file.read()
    puzzle = day.Puzzle()
    puzzle.puzzle_input = puzzle_input
    puzzle.solve()
    print(f"Part 1 answer: {puzzle.part_one_answer}")
    print(f"Part 2 answer: {puzzle.part_two_answer}")


if __name__ == "__main__":
    main()
