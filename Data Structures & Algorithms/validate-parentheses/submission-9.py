class Solution:
    def isValid(self, s: str) -> bool:
        pdict = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != pdict[s[i]]:
                    return False
                stack.pop()
        return len(stack) == 0