from base_puzzle import BasePuzzle
import more_itertools


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
        self.part_one_sample_correct_answer = 1588
        self.part_two_sample_correct_answer = 2188189693529
        self.part_one_correct_answer = 2590
        self.part_two_correct_answer = 2875665202438
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        starting_polymer, insertion_rules = puzzle_input.split("\n\n")
        insertion_rules = [rule.strip() for rule in insertion_rules.splitlines()]
        insertion_rules = [(pair, insertion) for pair, insertion in [rule.split(" -> ") for rule in insertion_rules]]

        polymer = starting_polymer

        for step in range(10):
            # print(get_pair_histogram(polymer))
            # print(step)
            staged_insertions: [[int, str]] = []
            for i, pair in enumerate(more_itertools.windowed(polymer, 2)):
                pair = "".join(pair)
                for rule in insertion_rules:
                    if pair == rule[0]:
                        staged_insertions.append((i + 1, rule[1]))

            insertions_done = 0
            for staged_insertion in staged_insertions:
                polymer = polymer[:staged_insertion[0] + insertions_done] + staged_insertion[1] + \
                          polymer[staged_insertion[0] + insertions_done:]
                insertions_done += 1

        bases = set(polymer)
        base_counts = {base: polymer.count(base) for base in bases}
        answer1 = max(base_counts.values()) - min(base_counts.values())

        rule_to_new_rules_map = {}
        for rule in insertion_rules:
            new_rule1 = None
            new_rule2 = None
            for rule2 in insertion_rules:
                if "".join([rule[0][0], rule[1]]) in rule2:
                    new_rule1 = rule2
                if "".join([rule[1], rule[0][1]]) in rule2:
                    new_rule2 = rule2
            rule_to_new_rules_map[rule] = (new_rule1, new_rule2)

        part_two_rule_histogram = {rule: 0 for rule in insertion_rules}
        part_two_base_histogram = {base: 0 for base in bases}

        for letter in starting_polymer:
            part_two_base_histogram[letter] += 1

        for i, pair in enumerate(more_itertools.windowed(starting_polymer, 2)):
            pair = "".join(pair)
            for rule in insertion_rules:
                if pair == rule[0]:
                    part_two_rule_histogram[rule] += 1

        for step in range(40):
            staged_rule_additions = {rule: 0 for rule in insertion_rules}
            for key, value in part_two_rule_histogram.items():
                new_rule1 = rule_to_new_rules_map[key][0]
                new_rule2 = rule_to_new_rules_map[key][1]
                part_two_base_histogram[key[1]] += value
                part_two_rule_histogram[key] -= value
                staged_rule_additions[new_rule1] += value
                staged_rule_additions[new_rule2] += value
            for key, value in staged_rule_additions.items():
                part_two_rule_histogram[key] += value

        answer2 = max(part_two_base_histogram.values()) - min(part_two_base_histogram.values())

        self.part_one_answer = answer1
        self.part_two_answer = answer2
