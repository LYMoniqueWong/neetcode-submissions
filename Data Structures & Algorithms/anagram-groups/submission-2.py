class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        seen = defaultdict(list)
        for i in strs:
            sorted_s = ''.join(sorted(i))
            seen[sorted_s].append(i)
        return list(seen.values())
