class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i, currCost): # returns the min cost to reacb top from cost[i]
            if i >= len(cost):
                return currCost
            if (i, currCost) in dp: return dp[(i, currCost)]
            currCost += cost[i]
            dp[(i, currCost)] = min(dfs(i+1, currCost), dfs(i+2, currCost))
            return dp[(i, currCost)]
        return min(dfs(0,0), dfs(1,0))