class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if i == '*':
                    stack.append(second_num*first_num)
                elif i == '+':
                    stack.append(second_num+first_num)
                elif i == '-':
                    stack.append(first_num-second_num)
                else:
                    stack.append(int(first_num/second_num))
        return stack[-1]
                

