class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            newDp = set()
            for j in dp:
                if nums[i] + j == target:
                    return True
                newDp.add(j)
                newDp.add(j+nums[i])
            dp = newDp
        return False