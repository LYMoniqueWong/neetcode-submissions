class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in b_dict:
                if stack and stack[-1] == b_dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        return len(stack) == 0