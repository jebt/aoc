import importlib
from os.path import splitext
from os import listdir
from time import perf_counter


def run_puzzle(year, puzzle_number, run_sample=True, run_real=True, timer=False):
    day = importlib.import_module(f"year_{year}.day_{str(puzzle_number).zfill(2)}")
    run_day_list([day], run_sample, run_real, timer=timer)


def run_all_puzzles(year, run_sample=True, run_real=True, timer=False):
    days = get_all_days_as_modules(year)
    error_count = run_day_list(days, run_sample, run_real, timer=timer)
    if error_count > 0:
        print(f"\nWARNING: At least 1 answer was INCORRECT! {error_count=}")


def run_day_list(days, run_sample=True, run_real=True, timer=False):
    start_time_day = None
    start_time_all = None
    day_to_time = {}
    if timer:
        start_time_all = perf_counter()
    error_count = 0
    for day in days:
        print(f"\n{day.__name__}")
        if run_sample:
            error_count += test_sample(day)
        if run_real:
            if timer:
                start_time_day = perf_counter()
            error_count += solve_puzzle(day)
            if timer:
                took = perf_counter() - start_time_day
                day_to_time[day.__name__] = took
                print(f"Day {day.__name__} took {took:.3f} seconds")
    if timer:
        if len(day_to_time) > 1:
            print(f"\nAll puzzles together took {perf_counter() - start_time_all:.3f} seconds")
            print(f"Average time per day: {sum(day_to_time.values()) / len(day_to_time):.3f} seconds")
            time_list = sorted(day_to_time.items(), key=lambda x: x[1])
            time_list = time_list[::-1]
            if len(time_list) > 3:
                print(f"Top 3 slowest days:")
                for day, time in time_list[:3]:
                    print(f"{day} took {time:.3f} seconds")

    return error_count


def get_all_days_as_modules(year):
    days = []
    for file in listdir(f"./year_{year}"):
        if splitext(file)[1] == ".py" and file.startswith("day_"):
            days.append(importlib.import_module(f"year_{year}.{file[:-3]}"))
            print(f"Imported year_{year}.{file[:-3]}")
    return days


def test_sample(day):
    error_count = 0
    puzzle_constructor = getattr(day, "Puzzle")
    puzzle = puzzle_constructor(use_sample_input=True)
    puzzle.solve()
    if puzzle.part_one_sample_correct_answer and puzzle.part_one_answer == puzzle.part_one_sample_correct_answer:
        print(f"Part 1 sample answer correct: {puzzle.part_one_answer}")
    elif puzzle.part_one_sample_correct_answer and \
            puzzle.part_one_answer != puzzle.part_one_sample_correct_answer:
        print(f"Part 1 sample answer INCORRECT: got {puzzle.part_one_answer}, "
              f"should be {puzzle.part_one_sample_correct_answer}")
        error_count += 1
    elif puzzle.part_one_answer:
        print(f"Part 1 sample answer: {puzzle.part_one_answer}")

    if puzzle.part_two_sample_correct_answer and puzzle.part_two_answer == puzzle.part_two_sample_correct_answer:
        print(f"Part 2 sample answer correct: {puzzle.part_two_answer}")
    elif puzzle.part_two_sample_correct_answer and \
            puzzle.part_two_answer != puzzle.part_two_sample_correct_answer:
        print(f"Part 2 sample answer INCORRECT: got {puzzle.part_two_answer}, "
              f"should be {puzzle.part_two_sample_correct_answer}")
        error_count += 1
    elif puzzle.part_two_answer:
        print(f"Part 2 sample answer: {puzzle.part_two_answer}")
    return error_count


def solve_puzzle(day):
    error_count = 0
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
        error_count += 1
    elif puzzle.part_one_answer:
        print(f"Part 1 answer: {puzzle.part_one_answer}")

    if puzzle.part_two_correct_answer and puzzle.part_two_answer == puzzle.part_two_correct_answer:
        print(f"Part 2 answer correct: {puzzle.part_two_answer}")
    elif puzzle.part_two_correct_answer and puzzle.part_two_answer != puzzle.part_two_correct_answer:
        print(f"Part 2 answer INCORRECT: got {puzzle.part_two_answer}, "
              f"should be {puzzle.part_two_correct_answer}")
        error_count += 1
    elif puzzle.part_two_answer:
        print(f"Part 2 answer: {puzzle.part_two_answer}")
    return error_count
