class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":   return 0
        res = 0
        l, r = 0, 1
        seen = set()
        seen.add(s[l])
        while r < len(s): # abc
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            res = max(res, r - l)
            seen.remove(s[l])
            l += 1
        res = max(res, r - l)
        return res
