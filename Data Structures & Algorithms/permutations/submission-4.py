class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue    
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False    
        backtrack([], [False]*len(nums))
        return res