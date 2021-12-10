from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
        self.part_one_sample_correct_answer = 15
        self.part_two_sample_correct_answer = 1134
        self.part_one_correct_answer = 560
        self.part_two_correct_answer = 959136
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        # point in grid: (height, is_low_point, part_of_basin_nr, is_top, is_bottom, is_left, is_right)
        grid = [[[int(x), False, None, False, False, False, False] for x in line] for line in lines]
        for i in range(len(grid)):
            grid[i][0][5] = True  # left
            grid[i][-1][6] = True  # right

        for i in range(len(grid[0])):
            grid[0][i][3] = True  # top
            grid[len(grid) - 1][i][4] = True  # bottom

        answer1 = 0
        low_points = []
        low_point_nr = 0
        for i, line in enumerate(lines):
            for j, spot in enumerate(line):
                is_top = False
                is_bottom = False
                is_left = False
                is_right = False
                lower_than_top = False
                lower_than_bottom = False
                lower_than_right = False
                lower_than_left = False
                height = int(spot)
                if i == 0:
                    is_top = True
                    lower_than_top = True
                elif i == len(lines) - 1:
                    is_bottom = True
                    lower_than_bottom = True
                if j == 0:
                    is_left = True
                    lower_than_left = True
                elif j == len(line) - 1:
                    is_right = True
                    lower_than_right = True
                if not is_top:
                    if height < int(lines[i - 1][j]):
                        lower_than_top = True
                if not is_bottom:
                    if height < int(lines[i + 1][j]):
                        lower_than_bottom = True
                if not is_left:
                    if height < int(lines[i][j - 1]):
                        lower_than_left = True
                if not is_right:
                    if height < int(lines[i][j + 1]):
                        lower_than_right = True
                if lower_than_top and lower_than_bottom and lower_than_right and lower_than_left:
                    is_low_point = True
                    low_point_nr += 1
                    answer1 += height + 1
                    low_points.append([height, is_low_point, low_point_nr, is_top, is_bottom, is_left, is_right, i, j])
                    grid[i][j] = [height, is_low_point, low_point_nr, is_top, is_bottom, is_left, is_right]

        changed = True
        while changed:
            changed = False
            for i, line in enumerate(grid):
                for j, spot in enumerate(line):
                    height = spot[0]
                    part_of_basin_nr = spot[2]
                    if height == 9 or part_of_basin_nr is None:
                        continue
                    else:
                        is_top = spot[3]
                        is_bottom = spot[4]
                        is_left = spot[5]
                        is_right = spot[6]
                        if not is_top:
                            if grid[i - 1][j][0] < 9 and grid[i - 1][j][2] is None:
                                grid[i - 1][j][2] = part_of_basin_nr
                                changed = True
                        if not is_bottom:
                            if grid[i + 1][j][0] < 9 and grid[i + 1][j][2] is None:
                                grid[i + 1][j][2] = part_of_basin_nr
                                changed = True
                        if not is_left:
                            if grid[i][j - 1][0] < 9 and grid[i][j - 1][2] is None:
                                grid[i][j - 1][2] = part_of_basin_nr
                                changed = True
                        if not is_right:
                            # print(i, j)
                            if grid[i][j + 1][0] < 9 and grid[i][j + 1][2] is None:
                                grid[i][j + 1][2] = part_of_basin_nr
                                changed = True

        # make a hashmap with the basin numbers as key and the frequency as value
        basin_nr_to_frequency = {}
        for line in grid:
            for spot in line:
                if spot[2] is not None:
                    if spot[2] in basin_nr_to_frequency:
                        basin_nr_to_frequency[spot[2]] += 1
                    else:
                        basin_nr_to_frequency[spot[2]] = 1

        # make a list of the basin numbers and their frequencies
        basin_nrs = []
        for basin_nr, frequency in basin_nr_to_frequency.items():
            basin_nrs.append([basin_nr, frequency])

        # sort the list by frequency
        basin_nrs.sort(key=lambda x: x[1], reverse=True)

        answer2 = basin_nrs[0][1] * basin_nrs[1][1] * basin_nrs[2][1]

        self.part_one_answer = answer1
        self.part_two_answer = answer2
