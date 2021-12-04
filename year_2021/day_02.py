from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
        self.part_one_sample_correct_answer = 150
        self.part_two_sample_correct_answer = 900
        self.part_one_correct_answer = 1250395
        self.part_two_correct_answer = 1451210346
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        part_one_answer, part_two_answer = loop_over_input(lines)
        self.part_one_answer = part_one_answer
        self.part_two_answer = part_two_answer


def loop_over_input(words):
    straight = 0
    depth = 0
    depth2 = 0
    aim = 0
    for i, word in enumerate(words):
        command = word.split(" ")
        direction = command[0]
        amount = int(command[1])
        if direction == "forward":
            straight += amount
            depth2 += (aim * amount)
        if direction == "down":
            depth += amount
            aim += amount
        if direction == "up":
            depth -= amount
            aim -= amount
    answer1 = straight * depth
    answer2 = straight * depth2
    return answer1, answer2
