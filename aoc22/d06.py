from more_itertools import all_unique, locate


def solution(input):
    return unique_window(input, 4), unique_window(input, 14)


def unique_window(iterable, window):
    return window + next(locate(iterable, lambda *x: all_unique(x), window))
