class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(curr, i, total):    # returns valid comb
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            backtrack(curr, i + 1, total + candidates[i])
            curr.pop()
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            backtrack(curr, i + 1, total)
        backtrack([], 0, 0)
        return res