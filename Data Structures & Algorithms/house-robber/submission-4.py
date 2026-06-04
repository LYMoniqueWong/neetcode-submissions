class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(len(nums)-1,-1,-1):
            tmp = max(nums[i]+rob2, rob1)
            rob2 = rob1
            rob1 = tmp
        return rob1
        
