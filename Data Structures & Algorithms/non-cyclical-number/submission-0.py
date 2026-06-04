class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1 and n not in visit:
            visit.add(n)
            res = 0
            while n > 0:
                digit = n % 10
                res += digit ** 2
                n = n // 10
            n = res
        return n == 1