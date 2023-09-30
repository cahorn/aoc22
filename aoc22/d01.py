from more_itertools import split_at


def solution(input):
    lines = input.splitlines()
    groups = split_at(lines, lambda l: l == "")
    elves = [sum(map(int, group)) for group in groups]
    elves.sort(reverse=True)
    return elves[0], sum(elves[0:3])
