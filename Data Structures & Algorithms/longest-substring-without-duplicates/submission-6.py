class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l, r = 0, 1
        ans = 0
        seen = set()
        seen.add(s[l])
        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            ans = max(ans, r-l)
            seen.remove(s[l])
            l += 1
        ans = max(ans, r-l)
        return ans