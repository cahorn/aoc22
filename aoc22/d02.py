def solution(input):
    part1 = part2 = 0
    for line in input.splitlines():
        first, second = line.split()
        # Normalize to 0 for rock/lose, 1 for paper/draw, 2 for scissors/win
        opponent, other = ord(first) - ord("A"), ord(second) - ord("X")
        part1 += score1(opponent, other)
        part2 += score2(opponent, other)
    return part1, part2


def score1(opponent, you):
    """
    Score a round of rock, paper, scissors as per part one.

    Some modular arithmetic shenanigans gives us an outcome value which is 0
    for a loss, 1 for a draw, and 2 for a win. The score can then be expressed
    purely mathematically without conditionals.
    """
    outcome = (you - opponent + 1) % 3
    return you + 1 + outcome * 3


def score2(opponent, outcome):
    """
    Score a round of rock, paper, scissors as per part two.

    This time the outcome is given, and it's your choice that must be derived;
    this can be easily done with some simple algebra to rearrange the outcome
    definition in part one.
    """
    you = (outcome + opponent - 1) % 3
    return you + 1 + outcome * 3
