class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        freq_list = [[] for i in range(len(nums)+1)]
        for num, freq in seen.items():
            freq_list[freq].append(num)
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res