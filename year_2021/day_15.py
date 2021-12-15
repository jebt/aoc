from base_puzzle import BasePuzzle
import networkx as nx


class Puzzle(BasePuzzle):
    def __init__(self, use_sample_input=False):
        super().__init__()
        # noinspection SpellCheckingInspection
        self.sample_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
        self.part_one_sample_correct_answer = 40
        self.part_two_sample_correct_answer = 315
        self.part_one_correct_answer = 583
        self.part_two_correct_answer = 2927
        self.use_sample_input = use_sample_input

    def solve(self):
        puzzle_input = self.sample_input if self.use_sample_input else self.puzzle_input
        lines = puzzle_input.splitlines()

        # a grid as a two-dimensional list of integers
        grid = []
        for line in lines:
            grid.append([int(x) for x in line])

        # turn the grid into a multi directed graph with the weights of the edges being the values of the nodes that
        # they travel to. First only add the nodes, then add the edges.
        graph = nx.MultiDiGraph()
        for y, line in enumerate(grid):
            for x, value in enumerate(line):
                graph.add_node((x, y), value=value)

        for y, line in enumerate(grid):
            for x, value in enumerate(line):
                if x > 0:
                    graph.add_edge((x, y), (x-1, y), weight=grid[y][x-1])
                if x < len(line) - 1:
                    graph.add_edge((x, y), (x+1, y), weight=grid[y][x+1])
                if y > 0:
                    graph.add_edge((x, y), (x, y-1), weight=grid[y-1][x])
                if y < len(grid) - 1:
                    graph.add_edge((x, y), (x, y+1), weight=grid[y+1][x])

        # find the path with the lowest total weight
        path = nx.dijkstra_path(graph, (0, 0), (len(grid)-1, len(grid)-1))

        # get the value of the first node in the path
        first_value = graph.nodes[path[0]]['value']

        total = 0
        for x, y in path:
            total += graph.nodes[(x, y)]['value']
        total -= first_value
        answer1 = total

        meta_grid = grid * 5
        for i, line in enumerate(meta_grid):
            meta_grid[i] = line * 5

        for y in range(len(meta_grid)):
            for x in range(len(meta_grid[y])):
                x_grid_steps = x//len(grid[0])
                y_grid_steps = y//len(grid)
                meta_grid[y][x] = update_weight(meta_grid[y][x], x_grid_steps + y_grid_steps)

        graph2 = nx.MultiDiGraph()
        for y, line in enumerate(meta_grid):
            for x, value in enumerate(line):
                graph2.add_node((x, y), value=value)

        for y, line in enumerate(meta_grid):
            for x, value in enumerate(line):
                if x > 0:
                    graph2.add_edge((x, y), (x - 1, y), weight=meta_grid[y][x - 1])
                if x < len(line) - 1:
                    graph2.add_edge((x, y), (x + 1, y), weight=meta_grid[y][x + 1])
                if y > 0:
                    graph2.add_edge((x, y), (x, y - 1), weight=meta_grid[y - 1][x])
                if y < len(meta_grid) - 1:
                    graph2.add_edge((x, y), (x, y + 1), weight=meta_grid[y + 1][x])

        # find the path with the lowest total weight
        path2 = nx.dijkstra_path(graph2, (0, 0), (len(meta_grid[0]) - 1, len(meta_grid) - 1))

        total = 0
        for x, y in path2:
            total += graph2.nodes[(x, y)]['value']
        total -= first_value

        answer2 = total
        self.part_one_answer = answer1
        self.part_two_answer = answer2


def update_weight(weight: int, steps: int) -> int:
    return 1 + ((weight + steps-1) % 9)
