class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, output = len(nums), []
        def backtrack(first):
            if first == n: 
                output.append(nums[:])
                return
            # try each available element in the 'first' slot
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return output