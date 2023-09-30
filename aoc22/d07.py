def solution(input):
    sizes = directory_sizes(iter(input.splitlines()))
    part1 = sum(filter(lambda d: d <= 100000, sizes))
    needed = 30000000 - (70000000 - sizes[-1])
    part2 = min(filter(lambda d: d >= needed, sizes))
    return part1, part2


def directory_sizes(lines):
    """
    Caluclate the size of each directory via a recusive in-order traversal.

    Note that the lines parameter is an pass-by-reference input iterator
    intended to be mutated as it traveses the call tree.
    """
    sizes = []
    size = 0
    try:
        line = next(lines)
        while line != "$ cd ..":
            if line == "$ ls" or line.startswith("dir"):
                pass  # noop
            elif line[0].isdigit():
                size += int(line.split()[0])
            elif line.startswith("$ cd"):
                sizes.extend(directory_sizes(lines))
                size += sizes[-1]
            line = next(lines)
    except StopIteration:
        pass
    sizes.append(size)
    return sizes
