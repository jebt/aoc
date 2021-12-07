from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """16,1,2,0,4,2,7,1,2,14"""
        self.part_one_sample_correct_answer = 37
        self.part_two_sample_correct_answer = 168
        self.part_one_correct_answer = None
        self.part_two_correct_answer = None
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input

        # split the input into a list of ints
        puzzle_input = puzzle_input.split(",")
        puzzle_input = [int(x) for x in puzzle_input]

        # determine the highest and lowest values in the input
        highest_value = max(puzzle_input)
        lowest_value = min(puzzle_input)

        # determine the sum of the difference of all the values in the input compared to all the values between the
        # highest and lowest values and keep track of the value that gives the lowest difference
        lowest_difference = None
        for i in range(lowest_value, highest_value + 1):
            fuel_cost = sum(abs(x - i) for x in puzzle_input)
            if lowest_difference is None or fuel_cost < lowest_difference:
                lowest_difference = fuel_cost

        def apply_weight(value):
            result = 0
            for index in range(value):
                result = result + value - index
            return result

        # same as above but the difference is weighted heavier for values that are further away from the range that
        # it is compared to. Each integer step 1 more.
        lowest_difference_weighted = None
        for i in range(lowest_value, highest_value + 1):
            fuel_cost = sum(apply_weight((abs(x - i))) for x in puzzle_input)
            if lowest_difference_weighted is None or fuel_cost < lowest_difference_weighted:
                lowest_difference_weighted = fuel_cost

        self.part_one_answer = lowest_difference
        self.part_two_answer = lowest_difference_weighted
