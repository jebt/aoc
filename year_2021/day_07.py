# todo: optimize with higher/lower divide and conquer strategy

from base_puzzle import BasePuzzle
# from time import perf_counter


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """16,1,2,0,4,2,7,1,2,14"""
        self.part_one_sample_correct_answer = 37
        self.part_two_sample_correct_answer = 168
        self.part_one_correct_answer = 325528
        self.part_two_correct_answer = 85015836
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
        for horizontal_position in range(lowest_value, highest_value + 1):
            fuel_cost = sum(abs(x - horizontal_position) for x in puzzle_input)
            if lowest_difference is None or fuel_cost < lowest_difference:
                lowest_difference = fuel_cost

        def apply_weight(value):
            return value * (value + 1) // 2

        # same as above but the difference is weighted heavier for values that are farther away from the range that
        # it is compared to. Each integer step 1 more.
        lowest_difference_weighted = None
        # start_time = perf_counter()
        # hashmap with the distance as the key and distance with the weight applied for fuel cost as the value
        # for memoization
        value_weight_map = {}
        for horizontal_position in range(lowest_value, highest_value + 1):
            # fuel_cost = sum(apply_weight((abs(x - horizontal_position))) for x in puzzle_input)
            fuel_cost = 0
            for crab in puzzle_input:
                distance = abs(crab - horizontal_position)
                if distance in value_weight_map:
                    fuel_cost += value_weight_map[distance]
                else:
                    individual_fuel_cost = apply_weight(distance)
                    fuel_cost += individual_fuel_cost
                    value_weight_map[distance] = individual_fuel_cost
                # fuel_cost = fuel_cost + apply_weight((abs(crab - horizontal_position)))
                if lowest_difference_weighted and fuel_cost > lowest_difference_weighted:
                    break
            if lowest_difference_weighted is None or fuel_cost < lowest_difference_weighted:
                lowest_difference_weighted = fuel_cost
        # end_time = perf_counter()
        # print(f"Time to calculate the weighted fuel cost: {end_time - start_time}")

        self.part_one_answer = lowest_difference
        self.part_two_answer = lowest_difference_weighted

        # print(value_weight_map)
