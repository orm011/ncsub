import math

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # note. naive approach: 
        # accumulation: loop and apply product n times.
        # O(n) time.
        # O(1) space.
        # better apporach: decompose into smaller subproblems.
        # myPow(x,n) ~= myPow(x,n//2)* myPow(x,n//2) * mypow(x,n%2)
        # Akshually note:
        # note floating point is not always associative as precision 
        # gets lost differently at differnt number sizes
        # differences between both apporaches. (but we have that
        # x^n is near 10^4, which i think may preserve accuracy fully()

        # recursive approach with re-use takes O(1) each step, 
        # for log_2(n) steps at most.
        # takes O(log n) stack space (number of bits, limited to 31)
        

        # if power is 111 in binary, n = 1*2**2 + 1*2**1 + 1*2**0 
        # lets go for stack based to balance practicality
        # this is equivalent to handling the total 
        # for n1 = 1*2**1 + 1*2**0, 
        # multiplying that total by itself, then by x once.
        # imagine n = 1000: we get that from setting
        # total = x # n = 0001
        # total = total * total # n = 0010
        # total = total * total # n = 0100
        # total = total * total # n = 1000

        # imagine n = 1001:
        # we start as before. 
        # but at the end 
        # total *= x

        # imagine n = 1010:
        # 1
        # 10 # itself
        # 101 # itself * x
        # 1010 #itself

        x, n = (x, n) if n >= 0 else (1/x, -n)

        total = 1

        # most significant bit to down
        for i in range(31, -1, -1): # 30, 29 .... 0 (31 bits to handle -2^31)
            bit = n & (1 << i) 
            total *= (total * x) if bit else total
            # while bits are 0, stays at 1.
            # msb: x. 
        
        return total
            


        