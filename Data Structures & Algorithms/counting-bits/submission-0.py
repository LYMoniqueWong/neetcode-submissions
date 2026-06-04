class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            res = 0
            while n:
                res += n % 2
                n = n >> 1
            return res
        output = []
        for i in range(n+1):
            output.append(countOnes(i)) 
        return output