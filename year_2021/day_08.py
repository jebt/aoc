from base_puzzle import BasePuzzle

zero_pattern = None
one_pattern = None
two_pattern = None
three_pattern = None
four_pattern = None
five_pattern = None
six_pattern = None
seven_pattern = None
eight_pattern = None
nine_pattern = None


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
        self.part_one_sample_correct_answer = 26
        self.part_two_sample_correct_answer = 61229
        self.part_one_correct_answer = 274
        self.part_two_correct_answer = 1012089
        self.use_sample_input = use_sample_input

    def solve(self):
        global zero_pattern, one_pattern, two_pattern, three_pattern, four_pattern, five_pattern, six_pattern, \
            seven_pattern, eight_pattern, nine_pattern
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        one_bars = 2
        seven_bars = 3
        four_bars = 4
        eight_bars = 7

        easy_digits = 0
        for i, line in enumerate(lines):
            line_first_part, line_second_part = line.split('|')
            output_digits = line_second_part.strip().split()
            for j, digit in enumerate(output_digits):
                length = len(digit)
                if length == one_bars or length == seven_bars or length == four_bars or length == eight_bars:
                    easy_digits += 1
        answer1 = easy_digits

        # zero = [0, 1, 2, 4, 5, 6]
        # one = [2, 5]
        # two = [0, 2, 3, 4, 6]
        # three = [0, 2, 3, 5, 6]
        # four = [1, 2, 3, 5]
        # five = [0, 1, 3, 5, 6]
        # six = [0, 1, 3, 4, 5, 6]
        # seven = [0, 2, 5]
        # eight = [0, 1, 2, 3, 4, 5, 6]
        # nine = [0, 1, 2, 3, 5, 6]

        # determining of patterns
        def determine_patterns(to_decode_patterns):
            global zero_pattern, one_pattern, two_pattern, three_pattern, four_pattern, five_pattern, six_pattern, \
                seven_pattern, eight_pattern, nine_pattern
            zero_pattern = None
            one_pattern = None
            two_pattern = None
            three_pattern = None
            four_pattern = None
            five_pattern = None
            six_pattern = None
            seven_pattern = None
            eight_pattern = None
            nine_pattern = None

            # easy digits
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == one_bars:
                    one_pattern = pattern
                if pattern_length == seven_bars:
                    seven_pattern = pattern
                if pattern_length == four_bars:
                    four_pattern = pattern
                if pattern_length == eight_bars:
                    eight_pattern = pattern

            # 3
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == 5 and x_contains_y(pattern, one_pattern):
                    three_pattern = pattern

            # 9
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == 6 and x_contains_y(pattern, four_pattern):
                    nine_pattern = pattern

            # 5
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == 5 and x_contains_y(nine_pattern, pattern) and pattern != three_pattern:
                    five_pattern = pattern

            # 2
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == 5 and pattern != three_pattern and pattern != five_pattern:
                    two_pattern = pattern

            # 0 and 6
            for pattern in to_decode_patterns:
                pattern_length = len(pattern)
                if pattern_length == 6 and x_contains_y(pattern, five_pattern) and \
                        not x_contains_y(pattern, one_pattern):
                    six_pattern = pattern
                elif pattern_length == 6 and not x_contains_y(pattern, five_pattern):
                    zero_pattern = pattern

        # deciphering and adding output digits
        total = 0
        for i, line in enumerate(lines):
            line_first_part, line_second_part = line.split('|')
            patterns = line_first_part.strip().split()
            output_digits = line_second_part.strip().split()
            determine_patterns(patterns)
            output_string = ''
            for output_digit in output_digits:
                if sorted(output_digit) == sorted(str(zero_pattern)):
                    output_string += '0'
                elif sorted(output_digit) == sorted(str(one_pattern)):
                    output_string += '1'
                elif sorted(output_digit) == sorted(str(two_pattern)):
                    output_string += '2'
                elif sorted(output_digit) == sorted(str(three_pattern)):
                    output_string += '3'
                elif sorted(output_digit) == sorted(str(four_pattern)):
                    output_string += '4'
                elif sorted(output_digit) == sorted(str(five_pattern)):
                    output_string += '5'
                elif sorted(output_digit) == sorted(str(six_pattern)):
                    output_string += '6'
                elif sorted(output_digit) == sorted(str(seven_pattern)):
                    output_string += '7'
                elif sorted(output_digit) == sorted(str(eight_pattern)):
                    output_string += '8'
                elif sorted(output_digit) == sorted(str(nine_pattern)):
                    output_string += '9'

            total = total + int(output_string)
        answer2 = total

        self.part_one_answer = answer1
        self.part_two_answer = answer2


def x_contains_y(x, y):
    for bar in y:
        if bar in x:
            continue
        else:
            return False
    return True
