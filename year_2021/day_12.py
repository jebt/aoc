from base_puzzle import BasePuzzle
import networkx as nx


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
        self.part_one_sample_correct_answer = 10
        self.part_two_sample_correct_answer = 36
        self.part_one_correct_answer = 5076
        self.part_two_correct_answer = None
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()
        g = nx.Graph()

        for i, line in enumerate(lines):
            from_cave, to_cave = line.split('-')
            g.add_edge(from_cave, to_cave)

        # A function to find the number of possible paths from start to end. If the node is in capitals it is allowed
        # to be visited any number of times. If the node is in lowercase it is only allowed to be visited once.
        def find_paths(graph, start, end, visited=None, path_so_far=None):
            if path_so_far is None:
                path_so_far = []
            if visited is None:
                visited = set()
            if start in visited:
                return 0
            if start == 'end':
                path_so_far.append(start)
                paths_list.append(path_so_far)
                return 1
            if start.islower():
                visited.add(start)
            paths = 0
            for node in g.neighbors(start):
                paths += find_paths(graph, node, end, visited.copy(), path_so_far + [start])
            return paths

        # The same as the function above except this time a single lowercase cave is allowed to be visited twice.
        # The start and end caves are still only allowed to be visited once.
        def find_paths_twice(graph, start, end, visited=None, path_so_far=None):
            second_time = False
            if path_so_far is None:
                path_so_far = []
            if visited is None:
                visited = set()
            if start in visited:
                second_time = True
                if start == 'start' or start == 'end':
                    return 0
                if "2" in visited:
                    return 0
            if start == 'end':
                path_so_far.append(start)
                paths_list.append(path_so_far)
                return 1
            if start.islower():
                if not second_time:
                    visited.add(start)
                else:
                    visited.add("2")
            paths = 0
            for node in g.neighbors(start):
                paths += find_paths_twice(graph, node, end, visited.copy(), path_so_far + [start])
            return paths

        paths_list = []
        answer1 = find_paths(g, 'start', 'end')
        answer2 = find_paths_twice(g, 'start', 'end')

        self.part_one_answer = answer1
        self.part_two_answer = answer2

