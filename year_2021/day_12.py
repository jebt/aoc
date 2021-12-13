from base_puzzle import BasePuzzle
import networkx as nx
# todo: DFS, instead of BFS with a single queue (popping after the recursive call to undo the changes)


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
        self.part_two_correct_answer = 145643
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
                paths.append(path_so_far)
                return 1
            if start.islower():
                visited.add(start)
            path_count = 0
            for node in g.neighbors(start):
                path_count += find_paths(graph, node, end, visited.copy(), path_so_far + [start])
            return path_count

        # The same as the function above except this time a single lowercase cave is allowed to be visited twice.
        # The start and end caves are still only allowed to be visited once.
        def find_paths2(graph, start, end, visited_lower_case_caves=None, path_so_far=None):
            if path_so_far is None:
                path_so_far = []
            if visited_lower_case_caves is None:
                visited_lower_case_caves = set()
            if start in visited_lower_case_caves:
                if "a_lower_case_cave_for_the_second_time" in visited_lower_case_caves or start in ["start", "end"]:
                    return 0
                second_time_in_lower_case_cave = True
            else:
                second_time_in_lower_case_cave = False
            if start == 'end':
                path_so_far.append(start)
                paths.append(path_so_far)
                return 1
            if start.islower():
                if not second_time_in_lower_case_cave:
                    visited_lower_case_caves.add(start)
                else:
                    visited_lower_case_caves.add("a_lower_case_cave_for_the_second_time")
            path_count = 0
            for node in g.neighbors(start):
                path_count += find_paths2(graph, node, end, visited_lower_case_caves.copy(), path_so_far + [start])
            return path_count

        paths = []
        answer1 = find_paths(g, 'start', 'end')
        answer2 = find_paths2(g, 'start', 'end')

        self.part_one_answer = answer1
        self.part_two_answer = answer2
