class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for i in nums:
            seen[i] += 1
        seen_list = list(seen.items())
        seen_list.sort(key=lambda x: (x[1], x[0]))
        ans = []
        for i in range(-1, -1-k, -1):
            ans.append(seen_list[i][0])
        return ans