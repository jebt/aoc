from base_puzzle import BasePuzzle

TIMER_AFTER_GIVING_BIRTH = 6
TIMER_AFTER_BEING_BORN = 8


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """3,4,3,1,2"""
        self.part_one_sample_correct_answer = 5934
        self.part_two_sample_correct_answer = 26984457539
        self.part_one_correct_answer = 377263
        self.part_two_correct_answer = 1695929023803
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        timers = [int(x) for x in puzzle_input.split(',')]
        aggregated_timers = [0 for _ in range(TIMER_AFTER_BEING_BORN+1)]
        for timer in timers:
            aggregated_timers[timer] += 1

        answer1 = calculate_amount_of_fish(aggregated_timers, generations=80)
        answer2 = calculate_amount_of_fish(aggregated_timers, generations=256)

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def calculate_amount_of_fish(input_timers, generations):
    aggregated_timers = input_timers.copy()
    for _ in range(generations):
        timers_on_zero = aggregated_timers[0]
        for i, timers in enumerate(aggregated_timers[:-1]):
            aggregated_timers[i] = aggregated_timers[i + 1]
        aggregated_timers[TIMER_AFTER_GIVING_BIRTH] += timers_on_zero
        aggregated_timers[TIMER_AFTER_BEING_BORN] = timers_on_zero
    total = 0
    for timer in aggregated_timers:
        total += timer
    return total
