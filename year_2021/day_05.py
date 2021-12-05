import itertools
from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
        self.part_one_sample_correct_answer = 5
        self.part_two_sample_correct_answer = 12
        self.part_one_correct_answer = 6564
        self.part_two_correct_answer = 19172
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()
        grid = [[0 for _ in range(1000)] for _ in range(1000)]

        # part one: only the horizontal and vertical lines
        for i, line in enumerate(lines):
            start_point, end_point = get_start_and_end_point(line)
            if start_point[0] == end_point[0] or start_point[1] == end_point[1]:
                draw_line(grid, start_point, end_point)
        answer1 = count_2_or_more(grid)

        # part two: add the diagonal lines
        for i, line in enumerate(lines):
            start_point, end_point = get_start_and_end_point(line)
            if start_point[0] != end_point[0] and start_point[1] != end_point[1]:
                draw_line(grid, start_point, end_point)
        answer2 = count_2_or_more(grid)

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def get_start_and_end_point(line):
    parts = line.split(' -> ')
    from_x, from_y = parts[0].split(',')
    to_x, to_y = parts[1].split(',')
    start_point = (int(from_x), int(from_y))
    end_point = (int(to_x), int(to_y))
    return start_point, end_point


def draw_line(grid, start_point, end_point):
    horizontal_range = inclusive_range(start_point[0], end_point[0])
    vertical_range = inclusive_range(start_point[1], end_point[1])
    fillvalue = None
    if len(horizontal_range) == 1:
        fillvalue = horizontal_range[0]
    elif len(vertical_range) == 1:
        fillvalue = vertical_range[0]
    for x, y in itertools.zip_longest(horizontal_range, vertical_range, fillvalue=fillvalue):
        grid[x][y] += 1


def inclusive_range(start, end):
    if start == end:
        return [start]
    elif end > start:
        return range(start, end + 1)
    elif end < start:
        return range(start, end - 1, -1)


def count_2_or_more(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell >= 2:
                count += 1
    return count
