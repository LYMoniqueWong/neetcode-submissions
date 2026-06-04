class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 0
        count = {}
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            window_length = r - l + 1
            most_freq_ch = max(count.values())
            if ((window_length - most_freq_ch) <= k):
                res = max(res, window_length)
            else:
                count[s[l]] -= 1
                l += 1
            r += 1
        return res