class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]: return "0"
        a, b = len(num1), len(num2)
        output = [0] * (a+b)
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(a):
            for j in range(b):
                res = int(num1[i]) * int(num2[j])
                output[i+j] += res
                output[i+j+1] += (output[i+j] // 10)
                output[i+j] = output[i+j] % 10
        output, beg = output[::-1], 0
        while beg < len(output) and output[beg] == 0:
            beg += 1
        output = map(str, output[beg:])
        return "".join(output)
