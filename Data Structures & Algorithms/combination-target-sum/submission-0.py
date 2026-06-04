class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target: 
                res.append(cur.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            # inc nus[i] in the combination
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # x inc nums[i], but not adding anything else yet
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res