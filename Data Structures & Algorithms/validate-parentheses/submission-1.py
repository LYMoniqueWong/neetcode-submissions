class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0 and c in [')', '}', ']']:
                return False
            elif c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0