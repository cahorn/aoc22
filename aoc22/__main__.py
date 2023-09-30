import argparse
import importlib
import sys


parser = argparse.ArgumentParser(
    description="Advent of Code 2022 Solutions", prog="aoc22"
)
parser.add_argument(
    "-d",
    "--day",
    choices=range(1, 26),
    help="day to run",
    metavar="DAY",
    required=True,
    type=int,
)
parser.add_argument(
    "-p",
    "--part",
    choices=[1, 2],
    help="part to run",
    metavar="PART",
    type=int,
)
parser.add_argument(
    "-f",
    "--file",
    default=sys.stdin,
    help="file from which to read input (default=stdin)",
    type=open,
)


def main():
    """Run the a selected solution over a given input and print the answer."""
    args = parser.parse_args()
    day = importlib.import_module(f"aoc22.d{args.day:02}")
    part1, part2 = day.solution(args.file.read())
    if args.part is None:
        print(f"Part 1: {part1}, Part 2: {part2}")
    elif args.part == 1:
        print(part1)
    else:
        print(part2)


if __name__ == "__main__":
    main()
