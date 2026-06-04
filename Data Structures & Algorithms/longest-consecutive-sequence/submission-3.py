class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet, res = set(nums), 0
        for n in numsSet:
            if n-1 not in numsSet:  # start of seq
                length = 1
                while n+length in numsSet:
                    length += 1
                res = max(res, length)
        return res