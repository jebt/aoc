from base_puzzle import BasePuzzle


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        self.sample_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
        self.part_one_sample_correct_answer = 4512
        self.part_two_sample_correct_answer = 1924
        self.part_one_correct_answer = 46920
        self.part_two_correct_answer = 12635
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()
        numbers_drawn = lines[0].split(',')
        board_lines = lines[2:]

        answer1 = None
        answer2 = None
        board_nr = 0
        board_line_nr = 0
        boards = []
        single_board = []
        for i, board_line in enumerate(board_lines):
            if board_line == '':
                boards.append(single_board)
                single_board = []
                board_nr += 1
                board_line_nr = 0
                continue
            else:
                single_board.append([])
                for j, number_str in enumerate(board_line.split()):
                    number = int(number_str)
                    single_board[board_line_nr].append([number, False])
                board_line_nr += 1
        boards.append(single_board)

        bingo = False
        first_winner_won = False
        for i, number_drawn_str in enumerate(numbers_drawn):
            if bingo:
                break
            number_drawn = int(number_drawn_str)
            for board in boards:
                mark_number_drawn(board, number_drawn)
            for j, board in enumerate(boards):
                if check_bingo(board):
                    if len(boards) == 1:
                        # print(f'BINGO on board {j}')
                        # print(f"number of draws: {i+1}, with number {number_drawn}")
                        # print(f"boards length: {len(boards)}")
                        sum_of_all_unmarked_numbers = get_sum_of_all_unmarked_numbers(board)
                        # print(sum_of_all_unmarked_numbers)
                        # print(number_drawn)
                        answer2 = sum_of_all_unmarked_numbers * number_drawn
                        bingo = True
                    else:
                        boards.remove(board)
                        if not first_winner_won:
                            # print(f'FIRST bingo on board {j}')
                            answer1 = get_sum_of_all_unmarked_numbers(board) * number_drawn
                            first_winner_won = True

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def mark_number_drawn(board, number_drawn):
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if number[0] == number_drawn:
                board[i][j][1] = True


def check_bingo(board):
    for i, row in enumerate(board):
        if check_row(row):
            # print(f'BING ROW row {i}')
            return True
    for j, col in enumerate(board[0]):
        column = []
        for row in board:
            column.append(row[j])
        if check_row(column):
            # print(f'BING COLUMN col {j}')
            return True


def check_row(row):
    for number in row:
        if not number[1]:
            return False
    return True


def get_sum_of_all_unmarked_numbers(board):
    _sum = 0
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if not number[1]:
                _sum += number[0]
    return _sum
