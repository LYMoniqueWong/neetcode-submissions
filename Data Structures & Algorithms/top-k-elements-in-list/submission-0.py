class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # nb: # of appearance
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        freq = [[] for i in range(len(nums) + 1)]
        for nb, cnt in count.items():
            freq[cnt].append(nb)
        res = []
        for i in range(len(nums), 0, -1):
            for nb in freq[i]:
                res.append(nb)
                if len(res) == k:
                    return res