from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """sample line 1
sample line 2
sample line 3"""
        self.part_one_sample_correct_answer = None
        self.part_two_sample_correct_answer = None
        self.part_one_correct_answer = None
        self.part_two_correct_answer = None
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        answer1 = None
        answer2 = None
        for i, line in enumerate(lines):
            print(i, line)
        self.part_one_answer = answer1
        self.part_two_answer = answer2
