class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a, b = len(s), len(t)
        if a < b:   return ""
        if s == t : return s
        countT, countS = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        l = 0
        res, lenRes = [-1, -1], float('inf')
        have, need = 0, len(countT)
        for r, ch in enumerate(s):
            if ch in countT:
                countS[ch] += 1
                if countS[ch] == countT[ch]:
                    have += 1
            while have == need:
                if (r-l+1) < lenRes:
                    lenRes = r-l+1
                    res = [l, r]
                if s[l] in countT:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if lenRes != float('inf') else ""
