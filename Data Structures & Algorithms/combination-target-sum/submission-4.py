class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, curr = [], []
        self.currSum = 0
        def dfs(i):
            if self.currSum == target:
                res.append(curr.copy())
                return
            if i == len(nums) or self.currSum > target:
                return
            curr.append(nums[i])
            self.currSum +=  nums[i]
            dfs(i)
            curr.pop()
            self.currSum -= nums[i]
            dfs(i+1)
        dfs(0)
        return res
            