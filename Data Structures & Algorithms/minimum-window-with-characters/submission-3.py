class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s): return ""
        if s == t:  return s
        
        countT, countS = {}, {}
        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r, ch in enumerate(s):
            if ch in countT:
                countS[ch] = 1 + countS.get(ch, 0)
                if countS[ch] == countT[ch]:
                    have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res, resLen = [l, r], r-l+1
                if s[l] in countT:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""