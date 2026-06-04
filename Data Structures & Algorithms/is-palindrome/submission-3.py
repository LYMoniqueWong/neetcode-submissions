class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] == " " or not s[l].isalnum():
                l += 1
                continue
            elif s[r] == " " or not s[r].isalnum():
                r -= 1
                continue
            elif s[l] != s[r]:    return False
            l += 1
            r -= 1
        return True