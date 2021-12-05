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

        # process_points(grid, lines)
        process_horizontal_and_vertical(grid, lines)
        answer1 = count_2_or_more(grid)

        process_diagonal(grid, lines)
        answer2 = count_2_or_more(grid)

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def draw_from_s_to_n(grid, start_point, end_point):
    for i in range(start_point[1], end_point[1] + 1):
        grid[start_point[0]][i] += 1


def draw_from_n_to_s(grid, start_point, end_point):
    for i in range(start_point[1], end_point[1] - 1, -1):
        grid[start_point[0]][i] += 1


def draw_from_w_to_e(grid, start_point, end_point):
    for i in range(start_point[0], end_point[0] + 1):
        grid[i][start_point[1]] += 1


def draw_from_e_to_w(grid, start_point, end_point):
    for i in range(start_point[0], end_point[0] - 1, -1):
        grid[i][start_point[1]] += 1


def draw_from_sw_to_ne(grid, start_point, end_point):
    length = abs(end_point[0] - start_point[0])
    for i in range(length+1):
        grid[start_point[0] + i][start_point[1] + i] += 1


def draw_from_se_to_nw(grid, start_point, end_point):
    length = abs(end_point[0] - start_point[0])
    for i in range(length+1):
        grid[start_point[0] - i][start_point[1] + i] += 1


def draw_from_nw_to_se(grid, start_point, end_point):
    length = abs(end_point[0] - start_point[0])
    for i in range(length+1):
        grid[start_point[0] + i][start_point[1] - i] += 1


def draw_from_ne_to_sw(grid, start_point, end_point):
    length = abs(end_point[0] - start_point[0])
    for i in range(length+1):
        grid[start_point[0] - i][start_point[1] - i] += 1


def process_points(grid, lines):
    for i, line in enumerate(lines):
        parts = line.split(' -> ')
        from_x, from_y = parts[0].split(',')
        to_x, to_y = parts[1].split(',')
        start_point = (int(from_x), int(from_y))
        end_point = (int(to_x), int(to_y))

        if start_point[0] == end_point[0] and start_point[1] == end_point[1]:
            grid[start_point[0]][start_point[1]] = 1


def process_horizontal_and_vertical(grid, lines):
    for i, line in enumerate(lines):
        parts = line.split(' -> ')
        from_x, from_y = parts[0].split(',')
        to_x, to_y = parts[1].split(',')
        start_point = (int(from_x), int(from_y))
        end_point = (int(to_x), int(to_y))

        # vertical
        if start_point[0] == end_point[0]:
            if start_point[1] < end_point[1]:
                draw_from_s_to_n(grid, start_point, end_point)
            if start_point[1] > end_point[1]:
                draw_from_n_to_s(grid, start_point, end_point)

        # horizontal
        if start_point[1] == end_point[1]:
            if start_point[0] < end_point[0]:
                draw_from_w_to_e(grid, start_point, end_point)
            if start_point[0] > end_point[0]:
                draw_from_e_to_w(grid, start_point, end_point)


def process_diagonal(grid, lines):
    for i, line in enumerate(lines):
        parts = line.split(' -> ')
        from_x, from_y = parts[0].split(',')
        to_x, to_y = parts[1].split(',')
        start_point = (int(from_x), int(from_y))
        end_point = (int(to_x), int(to_y))

        if start_point[0] < end_point[0] and start_point[1] < end_point[1]:
            draw_from_sw_to_ne(grid, start_point, end_point)
        if start_point[0] > end_point[0] and start_point[1] < end_point[1]:
            draw_from_se_to_nw(grid, start_point, end_point)
        if start_point[0] < end_point[0] and start_point[1] > end_point[1]:
            draw_from_nw_to_se(grid, start_point, end_point)
        if start_point[0] > end_point[0] and start_point[1] > end_point[1]:
            draw_from_ne_to_sw(grid, start_point, end_point)


def count_2_or_more(grid):
    count = 0
    for row in grid:
        for cell in row:
            if cell >= 2:
                count += 1
    return count
