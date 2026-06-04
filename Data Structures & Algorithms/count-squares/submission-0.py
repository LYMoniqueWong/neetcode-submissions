class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in list(self.pts):
            if (abs(x-px) != abs(y-py)) or x == px or y == py:
                continue
            res += self.pts[(x, y)] * self.pts[(px, y)] * self.pts[(x, py)]
        return res
