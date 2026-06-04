class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # rates
        res = max(piles) # min rate
        while l <= r:
            m = (l+r) // 2 # rate of m
            hours = 0
            for i in piles:
                hours += math.ceil(i/m)
            if hours <= h:
                res = m
                r = m - 1 # can try smaller k
            else: # need larger k
                l = m + 1
        return res