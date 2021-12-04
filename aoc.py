import year_2021.day_04 as day

from os.path import splitext


def main():
    test_sample()
    solve_puzzle()


def test_sample():
    puzzle = day.Puzzle(use_sample_input=True)
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


def solve_puzzle():
    with open(f"{splitext(day.__file__)[0]}_input.txt") as file:
        puzzle_input = file.read()
    puzzle = day.Puzzle(use_sample_input=False)
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
