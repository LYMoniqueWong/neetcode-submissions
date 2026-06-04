class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curr): # returns all the diff possible subsets of nums[i:]
            if i == len(nums):
                res.append(curr.copy())
                return
            # inc
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            # exc
            dfs(i+1, curr)
        dfs(0, [])
        return res