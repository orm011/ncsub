class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # least significant.
        n = len(digits)        
        i = n - 1
        
        # traverse right to left.
        # how do we handle extending the number
        # case where we must extend, 
        # traverse left
        carry = 1
        while carry and i >= 0:
            carry, digits[i] = divmod(digits[i] + carry, 10)
            i -= 1

        if not carry:
            return digits

        # traverse left
        digits.append(0) # add position

        for i in range(n + 1):
            tmp = digits[i]
            digits[i] = carry
            carry = tmp

        return digits








