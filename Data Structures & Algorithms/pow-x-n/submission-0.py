class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        res = 1
        for _ in range(n):
            res *= x
        return res