class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):   return False
        s1_dict, s2_dict = {}, {}
        for i in s1:
            s1_dict[i] = 1 + s1_dict.get(i, 0)
        l = 0
        for idx, r in enumerate(s2):
            if r not in s1_dict:
                s2_dict.clear()
                l = idx + 1
                continue
            s2_dict[r] = 1 + s2_dict.get(r, 0)
            while (idx-l+1) > len(s1):
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1
            if len(s1) == idx-l+1 and s1_dict == s2_dict:
                return True
        return False