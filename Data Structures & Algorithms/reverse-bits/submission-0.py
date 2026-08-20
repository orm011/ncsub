class Solution:
    def reverseBits(self, n: int) -> int:
        acc = 0
        pos = 31 # shift by 31 means 32 bits. 
        while n > 0:
            acc |= ((n & 1) << pos)
            n >>= 1
            pos -= 1
        return acc
            
