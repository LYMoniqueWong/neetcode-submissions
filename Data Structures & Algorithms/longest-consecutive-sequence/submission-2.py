class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        numsSet = set()
        for i in nums:
            numsSet.add(i)
        start = []
        for i in nums:
            if i-1 not in numsSet:
                start.append(i)
        res = 1
        for s in start:
            i, length = s, 1
            while i+1 in numsSet:
                length += 1
                i += 1
            res = max(res, length)
        return res