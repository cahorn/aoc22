import copy
import re

from more_itertools import split_at


def solution(input):
    stacks, moves = parse(input)
    stacks1, stacks2 = stacks, copy.deepcopy(stacks)
    for number, src, dest in moves:
        # Crate movement for part 1
        for i in range(number):
            stacks1[dest - 1].append(stacks1[src - 1].pop())
        # Crate movement for part 2
        stacks2[dest - 1].extend(stacks2[src - 1][-number:])
        stacks2[src - 1] = stacks2[src - 1][:-number]

    def top_crates(stacks):
        return "".join([stack[-1] for stack in stacks])

    return top_crates(stacks1), top_crates(stacks2)


def parse(input):
    stacks_input, moves_input = tuple(split_at(input.splitlines(), lambda l: l == ""))
    # Parse the diagram of the stacks of crates
    # (Has nobody heard of machine readability on this island!)
    stacks_number = int(stacks_input.pop().split()[-1])
    stacks = [list() for i in range(stacks_number)]
    for line in reversed(stacks_input):
        for i, crate in enumerate(line[1 : stacks_number * 4 : 4]):
            if crate != " ":
                stacks[i].append(crate)
    # Parse the moves list
    regex = re.compile("move (\d+) from (\d+) to (\d+)")
    moves = [tuple(map(int, regex.match(line).groups())) for line in moves_input]
    return stacks, moves
