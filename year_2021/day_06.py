from base_puzzle import BasePuzzle


# ans part 2 = estimated 49.178.108

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

        generations = 80
        sums = [0 for _ in range(9)]
        for timer in timers:
            sums[timer] += 1
        for gen in range(generations):
            amount_of_0 = sums[0]
            sums[0] = sums[1]
            sums[1] = sums[2]
            sums[2] = sums[3]
            sums[3] = sums[4]
            sums[4] = sums[5]
            sums[5] = sums[6]
            sums[6] = sums[7] + amount_of_0
            sums[7] = sums[8]
            sums[8] = amount_of_0
        total = 0
        for amount in sums:
            total += amount
        answer1 = total

        # for i in range(generations):
        #     if i % 9 == 0:
        #         print(len(timers))
        #         print(len([t for t in timers if t <= 1]))
        #     for j, timer in enumerate(timers):
        #         timers[j] = timers[j] - 1
        #         if timers[j] == -1:
        #             timers[j] = 6
        #             timers.append(9)

        # timers = [int(x) for x in puzzle_input.split(',')]
        # generations = 256
        # for i in range(generations):
        #     if i % 9 == 0:
        #         print(f"{i=}, {len(timers)=}")
        #         print(f"{len([t for t in timers if t <= 1])=}")
        #     for j, timer in enumerate(timers):
        #         timers[j] = timers[j] - 1
        #         if timers[j] == -1:
        #             timers[j] = 6
        #             timers.append(9)

        generations = 256
        sums = [0 for _ in range(9)]
        for timer in timers:
            sums[timer] += 1
        for gen in range(generations):
            amount_of_0 = sums[0]
            sums[0] = sums[1]
            sums[1] = sums[2]
            sums[2] = sums[3]
            sums[3] = sums[4]
            sums[4] = sums[5]
            sums[5] = sums[6]
            sums[6] = sums[7] + amount_of_0
            sums[7] = sums[8]
            sums[8] = amount_of_0
        total = 0
        for amount in sums:
            total += amount
        answer2 = total

        self.part_one_answer = answer1
        self.part_two_answer = answer2
