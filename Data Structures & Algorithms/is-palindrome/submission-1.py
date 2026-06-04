class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(s.split())).lower()
        x = ""
        for i in s:
            if i.isalnum():
                x += i
        l, r = 0, len(x)-1
        while l<r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True