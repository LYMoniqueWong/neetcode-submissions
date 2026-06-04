class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)        
        digits.reverse() # 19 -> 91 -> 02
        i, carry = 0, 1
        while i < n:
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
            i += 1
        if carry:
            digits.append(1)
        digits.reverse()
        return  digits