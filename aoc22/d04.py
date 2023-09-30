def solution(input):
    part1 = 0
    part2 = 0
    for line in input.splitlines():
        sections = list(map(int, line.replace("-", ",").split(",")))
        if subinterval(*sections):
            part1 += 1
        if overlap(*sections):
            part2 += 1
    return part1, part2


def subinterval(l1, r1, l2, r2):
    return l1 <= l2 <= r2 <= r1 or l2 <= l1 <= r1 <= r2


def overlap(l1, r1, l2, r2):
    return l1 <= l2 <= r1 or l2 <= l1 <= r2
