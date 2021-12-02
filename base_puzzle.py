class BasePuzzle:
    def __init__(self, day_nr=None, puzzle_input=None, sample_input="""sample line 1
sample line 2
sample line 3""", use_sample_input=False):
        self.day = day_nr
        self.puzzle_input = puzzle_input
        self.sample_input = sample_input
        self.part_one_answer = None
        self.part_two_answer = None
        self.use_sample_input = use_sample_input

    def set_puzzle_input(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def solve(self):
        print("Day {}:".format(self.day))
        print("not implemented yet")
