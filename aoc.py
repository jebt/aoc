from aoc_lib import *
import sys


YEAR = 2021
RUN_SAMPLE = True
RUN_REAL = True
TIMER = False


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("No arguments given, running all puzzles...\n")
        run_all_puzzles(year=YEAR, run_sample=RUN_SAMPLE, run_real=RUN_REAL, timer=TIMER)
    elif args[0] == "all":
        run_all_puzzles(year=YEAR, run_sample=RUN_SAMPLE, run_real=RUN_REAL, timer=TIMER)
    elif args[0] == "today":
        from datetime import date
        day = date.today().day
        run_puzzle(year=YEAR, puzzle_number=day, run_sample=RUN_SAMPLE, run_real=RUN_REAL, timer=TIMER)
    elif args[0].isdigit():
        try:
            puzzle_number = int(args[0])
            if puzzle_number < 1 or puzzle_number > 25:
                raise ValueError
            else:
                run_puzzle(year=YEAR, puzzle_number=puzzle_number, timer=TIMER)
        except ValueError:
            print(f"Invalid puzzle number: {args[0]}")
            print("Valid puzzle numbers are 1-25")
            return


if __name__ == "__main__":
    main()
