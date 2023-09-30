import importlib
import pathlib
import pytest

answers = {
    1: (24000, 45000),
}


@pytest.mark.parametrize("day,answer", answers.items())
def test_day(day, answer):
    with open(pathlib.Path(__file__).parent / f"d{day:02}.txt") as infile:
        module = importlib.import_module(f"aoc22.d{day:02}")
        assert answer == module.solution(infile.read())
