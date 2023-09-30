import importlib
import pathlib
import pytest

answers = {
    1: (24000, 45000),
    2: (15, 12),
    3: (157, 70),
    4: (2, 4),
    5: ("CMZ", "MCD"),
    6: (7, 19),
    7: (95437, 24933642),
    8: (21, 8),
}


@pytest.mark.parametrize("day,answer", answers.items())
def test_day(day, answer):
    with open(pathlib.Path(__file__).parent / f"d{day:02}.txt") as infile:
        module = importlib.import_module(f"aoc22.d{day:02}")
        assert answer == module.solution(infile.read())
