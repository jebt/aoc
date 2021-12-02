import os


class Puzzle:
    part_one_answer, part_two_answer = None, None

    def solve(self):
        with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
            puzzle_input = f.read()

        words = puzzle_input.split()
        # print(words)
        numbers = [int(word) for word in words]

        part_one_answer, part_two_answer = loop_over_input(numbers)
        self.part_one_answer = part_one_answer
        self.part_two_answer = part_two_answer
        # print(f"part one answer: {part_one_answer}")
        # print(f"part two answer: {part_two_answer}")


def main():
    old_solve()


def old_solve():
    pass


def loop_over_input(words):
    times_window_increased = 0
    times_single_increased = 0
    max_times_increased = 0
    for i, word in enumerate(words):
        if i < 1:
            continue
        elif i > 2 and (word + words[i-1] + words[i-2]) > (words[i-1] + words[i-2] + words[i-3]):
            times_window_increased += 1
            if times_window_increased > max_times_increased:
                max_times_increased = times_window_increased
        if word > words[i-1]:
            times_single_increased += 1
        else:
            pass
            # times_window_increased = 0
    return times_single_increased, times_window_increased


if __name__ == "__main__":
    main()
