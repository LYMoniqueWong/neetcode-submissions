class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        def countOnes(n):
            res = 0
            while n:
                res += n % 2
                n >>= 1
            return res
        for i in range(n+1):
            res.append(countOnes(i))
        return res