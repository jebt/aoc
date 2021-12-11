from base_puzzle import BasePuzzle
from collections import deque

character_scoring = {")": 3,
                     "]": 57,
                     "}": 1197,
                     ">": 25137}

part_two_scoring = {")": 1,
                    "]": 2,
                    "}": 3,
                    ">": 4}

opposites = {")": "(",
             "]": "[",
             "}": "{",
             ">": "<",
             "<": ">",
             "[": "]",
             "{": "}",
             "(": ")"}


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
        self.part_one_sample_correct_answer = 26397
        self.part_two_sample_correct_answer = 288957
        self.part_one_correct_answer = 315693
        self.part_two_correct_answer = 1870887234
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        score = 0
        corrupted_indexes = []
        for i, line in enumerate(lines):
            stack = deque()
            for char in line:
                if char in ")}]>":
                    if not stack:
                        score += character_scoring[char]
                        corrupted_indexes.append(i)
                        break
                    else:
                        if stack[-1] != opposites[char]:
                            score += character_scoring[char]
                            corrupted_indexes.append(i)
                            break
                        else:
                            stack.pop()
                elif char in "{[(<":
                    stack.append(char)
        answer1 = score

        non_corrupted_lines = [line for i, line in enumerate(lines) if i not in corrupted_indexes]
        scores2 = []
        for i, line in enumerate(non_corrupted_lines):
            stack = deque()
            line_score = 0
            for char in line:
                if char in "(<[{":
                    stack.append(char)
                elif char in ")}]>":
                    stack.pop()
            while stack:
                line_score = (line_score * 5) + part_two_scoring[opposites[stack.pop()]]
            scores2.append(line_score)

        scores2.sort()
        answer2 = scores2[len(scores2)//2]

        self.part_one_answer = answer1
        self.part_two_answer = answer2
