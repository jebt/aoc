from aoc_lib import *
import sys


YEAR = 2021
RUN_SAMPLE = True
RUN_REAL = True


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments given, running all puzzles...")
        run_all_puzzles(YEAR, RUN_SAMPLE, RUN_REAL)
    elif args[0] == "all":
        run_all_puzzles(YEAR)
    elif args[0] == "today":
        from datetime import date
        day = date.today().day
        run_puzzle(YEAR, day, RUN_SAMPLE, RUN_REAL)
    elif args[0].isdigit():
        try:
            puzzle_number = int(args[0])
            if puzzle_number < 1 or puzzle_number > 25:
                raise ValueError
            else:
                run_puzzle(YEAR, puzzle_number)
        except ValueError:
            print(f"Invalid puzzle number: {args[0]}")
            print("Valid puzzle numbers are 1-25")
            return


if __name__ == "__main__":
    main()
