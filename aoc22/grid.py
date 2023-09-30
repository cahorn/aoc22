import collections
import enum
import itertools


class Point(collections.namedtuple("Point", ["x", "y"], defaults=(0, 0))):
    __slots__ = ()

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def walk(self, dir, bounds=None):
        for i in itertools.count(1):
            point = self + dir.value * i
            if bounds is not None and not bounds[0] <= point < bounds[1]:
                break
            else:
                yield point


class Dir(enum.Enum):
    N = Point(0, 1)
    S = Point(0, -1)
    E = Point(1, 0)
    W = Point(-1, 0)
    U = N
    D = S
    R = E
    L = W
