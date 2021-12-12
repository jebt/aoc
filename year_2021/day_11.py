from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
        self.part_one_sample_correct_answer = 1656
        self.part_two_sample_correct_answer = 195
        self.part_one_correct_answer = 1571
        self.part_two_correct_answer = 387
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        grid = [[int(x) for x in line] for line in puzzle_input.splitlines()]

        flash_count = 0
        step_nr = 0
        answer1 = None
        while not all_flashed_simultaneously(grid):
            flash_count += step(grid)
            step_nr += 1
            if step_nr == 100:
                answer1 = flash_count

        answer2 = step_nr

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def step(grid):
    f_count = 0
    for i, line in enumerate(grid):
        for j, energy_level in enumerate(line):
            grid[i][j] = energy_level + 1
    changes = True
    while changes:
        changes = False
        for i, line in enumerate(grid):
            for j, energy_level in enumerate(line):
                if energy_level > 9:
                    grid[i][j] = 0
                    f_count += 1
                    for neighbour_energy, xx, yy in get_neighbours(grid, i, j):
                        if neighbour_energy == 0:
                            continue
                        else:
                            grid[xx][yy] = neighbour_energy + 1
                            changes = True
    return f_count


def get_neighbours(grid, x, y):
    neighbours = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                continue
            neighbours.append((grid[i][j], i, j))
    return neighbours


def all_flashed_simultaneously(grid):
    for i, line in enumerate(grid):
        for j, energy_level in enumerate(line):
            if energy_level != 0:
                return False
    return True
