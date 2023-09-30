from aoc22.grid import Dir, Point


def solution(input):
    trees = list(map(lambda l: list(map(int, l)), input.splitlines()))
    visible_trees = 0
    best_score = 0
    for y in range(len(trees)):
        for x in range(len(trees[0])):
            visible, score = view(trees, Point(x,y))
            visible_trees += 1 if visible else 0
            best_score = max(best_score, score)
    return visible_trees, best_score


def view(trees, start):
    visible = False
    score = 1
    for dir in Dir:
        bounds = (Point(), Point(len(trees[0]), len(trees)))
        i = 0
        for step in start.walk(dir, bounds=bounds):
            i += 1
            if trees[start.y][start.x] <= trees[step.y][step.x]:
                break
        else:
            visible = True
        score *= i
    return visible, score
