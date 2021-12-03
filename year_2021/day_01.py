from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """199
200
208
210
200
207
240
269
260
263"""
        self.part_one_sample_correct_answer = 7
        self.part_two_sample_correct_answer = 5
        self.part_one_correct_answer = 1754
        self.part_two_correct_answer = 1789
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input

        words = puzzle_input.split()
        numbers = [int(word) for word in words]

        part_one_answer, part_two_answer = loop_over_input(numbers)
        self.part_one_answer = part_one_answer
        self.part_two_answer = part_two_answer


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
    return times_single_increased, times_window_increased
