class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums): # can't rob adjacent, ignoring first & last constraint
            rob1, rob2 = 0, 0
            for i in nums:
                tmp = max(i+rob1, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
