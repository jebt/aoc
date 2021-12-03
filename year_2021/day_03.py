from base_puzzle import BasePuzzle
import unittest


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
        self.part_one_sample_correct_answer = 198
        self.part_two_sample_correct_answer = 230
        self.part_one_correct_answer = 1071734
        self.part_two_correct_answer = 6124992
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        bit_counts = [0 for _ in range(len(lines[0]))]
        for i, line in enumerate(lines):
            for j, bit in enumerate(line):
                if bit == '1':
                    bit_counts[j] += 1
        first_binary = ['1' if count >= (len(lines) / 2) else '0' for count in bit_counts]
        second_binary = ['1' if bit == '0' else '0' for bit in first_binary]
        first_binary = ''.join(first_binary)
        second_binary = ''.join(second_binary)
        answer1 = int(first_binary, 2) * int(second_binary, 2)

        # Part 2
        index = 0
        filtered_list = [line for line in lines]
        while len(filtered_list) > 1:
            most_common_bit = find_most_common_bit(index, filtered_list)
            filtered_list = [line for line in filtered_list if line[index] == most_common_bit]
            index += 1

        index2 = 0
        filtered_list2 = [line for line in lines]
        while len(filtered_list2) > 1:
            most_common_bit2 = find_most_common_bit(index2, filtered_list2)
            filtered_list2 = [line for line in filtered_list2 if line[index2] != most_common_bit2]
            index2 += 1

        filtered_list = ''.join(filtered_list)
        filtered_list2 = ''.join(filtered_list2)

        answer2 = int(filtered_list, 2) * int(filtered_list2, 2)
        self.part_one_answer = answer1
        self.part_two_answer = answer2


def find_most_common_bit(index, filtered_list):
    count_of_ones = 0
    for line in filtered_list:
        if line[index] == '1':
            count_of_ones += 1
    if count_of_ones >= (len(filtered_list) / 2):
        return '1'
    else:
        return '0'


class TestDay(unittest.TestCase):
    def test_part_one(self):
        puzzle = Puzzle()
        puzzle.use_sample_input = True
        puzzle.solve()
        self.assertEqual(puzzle.part_one_answer, puzzle.part_one_sample_correct_answer)

    def test_part_two(self):
        puzzle = Puzzle()
        puzzle.use_sample_input = True
        puzzle.solve()
        self.assertEqual(puzzle.part_two_answer, puzzle.part_two_sample_correct_answer)

        # self.assertEqual(puzzle.part_one_answer, puzzle.part_one_correct_answer)
        # self.assertEqual(puzzle.part_two_answer, puzzle.part_two_correct_answer)
        # self.assertEqual(puzzle.part_one_sample_answer, puzzle.part_one_sample_correct_answer)
        # self.assertEqual(puzzle.part_two_sample_answer, puzzle.part_two_sample_correct_answer)
