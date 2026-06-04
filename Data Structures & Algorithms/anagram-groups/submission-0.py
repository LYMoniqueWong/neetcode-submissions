class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_s = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            dict_s[tuple(count)].append(s)
        return list(dict_s.values())

