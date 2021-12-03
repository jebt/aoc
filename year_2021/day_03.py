from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self):
        super().__init__()
        self.sample_input = """sample line 1
sample line 2
sample line 3"""
        # self.use_sample_input = True

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        answer1 = None
        answer2 = None
        bit_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i, line in enumerate(lines):
            for j, bit in enumerate(line):
                if bit == '1':
                    bit_counts[j] += 1
        # print(len(lines))
        # print(bit_counts)
        first_binary = ['1' if count > 500 else '0' for count in bit_counts]
        # print(first_binary)
        second_binary = ['1' if bit == '0' else '0' for bit in first_binary]
        # print(second_binary)
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
            bit_to_keep = '0' if most_common_bit2 == '1' else '1'
            filtered_list2 = [line for line in filtered_list2 if line[index2] == bit_to_keep]
            index2 += 1

        print(filtered_list)
        print(filtered_list2)

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
