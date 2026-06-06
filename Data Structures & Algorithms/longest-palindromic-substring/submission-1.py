class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            # expand while chars match and in bounds
            # return longest palindrom from this center
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # odd length
            odd = expand(i, i)
            # even length
            even = expand(i, i+1)
            if len(odd) >= len(even) and len(odd) > len(res):
                res = odd
            elif len(even) > len(odd) and len(even) > len(res):
                res = even
        return res