import os

part_one_answer, part_two_answer = None, None


class Puzzle:
    part_one_answer, part_two_answer = None, None

    def solve(self):
        global part_one_answer, part_two_answer
        with open(f"{os.path.splitext(__file__)[0]}_input.txt") as f:
            puzzle_input = f.read()

        words = puzzle_input.split("\n")
        # numbers = [int(word) for word in words]

        part_one_answer, part_two_answer = loop_over_input(words)
        self.part_one_answer = part_one_answer
        self.part_two_answer = part_two_answer
        # print(f"part one answer: {part_one_answer}")
        # print(f"part two answer: {part_two_answer}")


def main():
    solve()


def solve():
    pass


def loop_over_input(words):
    straight = 0
    depth = 0
    depth2 = 0
    aim = 0
    words = words[:-1]
    for i, word in enumerate(words):
        command = word.split(" ")
        direction = command[0]
        amount = int(command[1])
        # print(f"{i}: {direction} {amount}")
        if direction == "forward":
            straight += amount
            depth2 += (aim * amount)
        if direction == "down":
            depth += amount
            aim += amount
        if direction == "up":
            depth -= amount
            aim -= amount
    answer1 = straight * depth
    answer2 = straight * depth2

    return answer1, answer2


if __name__ == "__main__":
    main()
