from base_puzzle import BasePuzzle


def get_sub_grid_letter(sub_grid):
    if sub_grid == ['###.', '#..#', '#..#', '###.', '#.#.', '#..#']:
        return 'R'
    elif sub_grid == ['####', '#...', '###.', '#...', '#...', '####']:
        return 'E'
    elif sub_grid == ['#..#', '#..#', '#..#', '#..#', '#..#', '.##.']:
        return 'U'
    elif sub_grid == ['#...', '#..#', '#..#', '#...', '#..#', '#..#']:
        return 'K'
    elif sub_grid == ['###.', '#..#', '#..#', '###.', '#...', '#...']:
        return 'P'
    elif sub_grid == ['#..#', '#.#.', '##..', '#.#.', '#.#.', '#..#']:
        return 'K'
    else:
        return '?'


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
        self.part_one_sample_correct_answer = 17
        self.part_two_sample_correct_answer = None
        self.part_one_correct_answer = 775
        # noinspection SpellCheckingInspection
        self.part_two_correct_answer = "REUPUPKR"
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        section_1, section_2 = puzzle_input.split("\n\n")
        points = [(int(x), int(y)) for x, y in [line.split(',') for line in section_1.splitlines()]]
        fold_directions = section_2.splitlines()
        fold_directions = [line.split()[2] for line in fold_directions]
        fold_directions = [(orientation, int(distance)) for
                           orientation, distance in [line.split('=') for line in fold_directions]]

        answer1 = None
        for i, direction in enumerate(fold_directions):
            if i == 1:
                answer1 = len(set(points))
            for j, point in enumerate(points):
                if direction[0] == 'x':
                    coordinate = point[0]
                else:
                    coordinate = point[1]
                if coordinate > direction[1]:
                    diff = coordinate - direction[1]
                    if direction[0] == 'x':
                        points[j] = (point[0] - diff*2, point[1])
                    else:
                        points[j] = (point[0], point[1] - diff*2)

        final_set = set(points)
        # now turn this set into a grid with hashes for points and dots for empty spaces
        grid = [['.' for _ in range(max(points, key=lambda x: x[1])[1] + 1)] for
                _ in range(max(points, key=lambda x: x[0])[0] + 1)]
        for point in final_set:
            grid[point[0]][point[1]] = '#'

        # turn the grid 90 degrees clockwise
        grid = [''.join(row) for row in zip(*grid[::-1])]

        # make a new grid that mirrors the content in the horizontal axis
        mirrored_grid = []
        for row in grid:
            mirrored_grid.append(row[::-1])

        # for line in mirrored_grid:  # this should print a human-readable access code (8 capital letters) in ascii art
        #     print(line)

        # make a list of 8 sub grids with original height but width of 4. Ignore 1 column between the sub grids
        sub_grids = []
        for i in range(8):
            x_start = i*5
            x_end = x_start + 4
            sub_grids.append([row[x_start:x_end] for row in mirrored_grid])

        # try to recognize a capital letter in each sub grid
        sub_grid_letters = []
        for sub_grid in sub_grids:
            sub_grid_letters.append(get_sub_grid_letter(sub_grid))

        answer2 = ''.join(sub_grid_letters)

        self.part_one_answer = answer1
        self.part_two_answer = answer2
