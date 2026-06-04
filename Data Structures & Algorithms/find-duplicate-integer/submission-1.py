class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,4,2,2]
        # 0 -> 1 -> 3 -> 2 <-> 4
        # node i points to node nums[i], for each i
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
