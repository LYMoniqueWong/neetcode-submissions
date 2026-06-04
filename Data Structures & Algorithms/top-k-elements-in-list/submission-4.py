class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int) # nb: freq
        for n in nums:
            seen[n] += 1
        buckets = defaultdict(list) # freq: [list of nbs]
        for key, val in seen.items():
            buckets[val].append(key)
        res = []
        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                res.extend(buckets[freq])
                if len(res) >= k:
                    return res[:k]