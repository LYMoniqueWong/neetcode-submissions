class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            if (i-1) not in s:
                start = i
                while start in s:
                    start += 1
                ans = max(ans, start-i)
        return ans