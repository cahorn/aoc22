from more_itertools import divide, chunked


def solution(input):
    lines = input.splitlines()
    rucksacks = [divide(2, line) for line in lines]
    misplaced = [shared(rucksack).pop() for rucksack in rucksacks]
    groups = chunked(lines, 3)
    badges = [shared(group).pop() for group in groups]
    return sum(map(priority, misplaced)), sum(map(priority, badges))


def shared(iterables):
    """Return the intersection set of the given iterables."""
    return set.intersection(*map(set, iterables))


def priority(item):
    return ord(item) - ord("a") + 1 if item.islower() else ord(item) - ord("A") + 27
