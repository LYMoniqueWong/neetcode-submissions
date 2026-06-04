class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1,3,4,2,2]
        # 0 --> 1 --> 3 --> 2 <--> 4
        # node i points to node nums[i], for each i
        # 0 -> 1
        # 1 -> 3
        # 2 -> 4
        # 3 -> 2
        # 4 -> 2

        s, f = 0, 0
        while True: # find where s & f intersects first
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s2 = 0
        while True:
            s = nums[s]
            s2 = nums[s2]
            if s == s2:
                return s
