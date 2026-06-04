class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 000
        # 001
        # 010
        count = set()
        for i in range(len(nums)+1):
            count.add(i)
        for i in nums:
            count.remove(i)
        for i in count:
            return i