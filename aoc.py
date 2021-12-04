import importlib
import sys
from os.path import splitext
from os import listdir

YEAR = 2021


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments given, running all puzzles")
        run_all_puzzles()
    elif args[0] == "all":
        run_all_puzzles()
    elif args[0] == "today":
        from datetime import date
        day = date.today().day
        run_puzzle(day)
    elif args[0].isdigit():
        try:
            puzzle_number = int(args[0])
            if puzzle_number < 1 or puzzle_number > 25:
                raise ValueError
            else:
                run_puzzle(puzzle_number)
        except ValueError:
            print(f"Invalid puzzle number: {args[0]}")
            print("Valid puzzle numbers are 1-25")
            return


def run_puzzle(puzzle_number):
    day = importlib.import_module(f"year_{YEAR}.day_{str(puzzle_number).zfill(2)}")
    print(f"\n{day.__name__}")
    test_sample(day)
    solve_puzzle(day)


def run_all_puzzles():
    days = get_all_days_as_modules()
    run_day_list(days)


def run_day_list(days):
    for day in days:
        print(f"\n{day.__name__}")
        test_sample(day)
        solve_puzzle(day)


def get_all_days_as_modules():
    days = []
    for file in listdir(f"./year_{YEAR}"):
        if splitext(file)[1] == ".py" and file.startswith("day_"):
            days.append(importlib.import_module(f"year_{YEAR}.{file[:-3]}"))
            print(f"Imported year_{YEAR}.{file[:-3]}")
    return days


def test_sample(day):
    puzzle_constructor = getattr(day, "Puzzle")
    puzzle = puzzle_constructor(use_sample_input=True)
    puzzle.solve()
    if puzzle.part_one_sample_correct_answer and puzzle.part_one_answer == puzzle.part_one_sample_correct_answer:
        print(f"Part 1 sample answer correct: {puzzle.part_one_answer}")
    elif puzzle.part_one_sample_correct_answer and \
            puzzle.part_one_answer != puzzle.part_one_sample_correct_answer:
        print(f"Part 1 sample answer INCORRECT: got {puzzle.part_one_answer}, "
              f"should be {puzzle.part_one_sample_correct_answer}")
    elif puzzle.part_one_answer:
        print(f"Part 1 sample answer: {puzzle.part_one_answer}")

    if puzzle.part_two_sample_correct_answer and puzzle.part_two_answer == puzzle.part_two_sample_correct_answer:
        print(f"Part 2 sample answer correct: {puzzle.part_two_answer}")
    elif puzzle.part_two_sample_correct_answer and \
            puzzle.part_two_answer != puzzle.part_two_sample_correct_answer:
        print(f"Part 2 sample answer INCORRECT: got {puzzle.part_two_answer}, "
              f"should be {puzzle.part_two_sample_correct_answer}")
    elif puzzle.part_two_answer:
        print(f"Part 2 sample answer: {puzzle.part_two_answer}")


def solve_puzzle(day):
    with open(f"{splitext(day.__file__)[0]}_input.txt") as file:
        puzzle_input = file.read()
    puzzle_constructor = getattr(day, "Puzzle")
    puzzle = puzzle_constructor(use_sample_input=False)
    puzzle.puzzle_input = puzzle_input
    puzzle.solve()
    if puzzle.part_one_correct_answer and puzzle.part_one_answer == puzzle.part_one_correct_answer:
        print(f"Part 1 answer correct: {puzzle.part_one_answer}")
    elif puzzle.part_one_correct_answer and puzzle.part_one_answer != puzzle.part_one_correct_answer:
        print(f"Part 1 answer INCORRECT: got {puzzle.part_one_answer}, "
              f"should be {puzzle.part_one_correct_answer}")
    elif puzzle.part_one_answer:
        print(f"Part 1 answer: {puzzle.part_one_answer}")

    if puzzle.part_two_correct_answer and puzzle.part_two_answer == puzzle.part_two_correct_answer:
        print(f"Part 2 answer correct: {puzzle.part_two_answer}")
    elif puzzle.part_two_correct_answer and puzzle.part_two_answer != puzzle.part_two_correct_answer:
        print(f"Part 2 answer INCORRECT: got {puzzle.part_two_answer}, "
              f"should be {puzzle.part_two_correct_answer}")
    elif puzzle.part_two_answer:
        print(f"Part 2 answer: {puzzle.part_two_answer}")


if __name__ == "__main__":
    main()
