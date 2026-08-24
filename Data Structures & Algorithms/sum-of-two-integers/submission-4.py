class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use bit operations. ..
        # XOR gives you the bitwise sum without the carry
        # carry comes from AND, then shift.
        # the carry then has to be added to the number...
        # where it may cause a new carry again.
        # we could go bit by bit: xor bit n, and bit n, shift.
        # xor bit n from both numbers and carry gives you final parity for thoese 3
        # what gives you the carry? need 2 or 3 bits.

        # how about negatives: they eventually become 111111

        # both a b are within -1024 and 1023: 
        # the addition is then bound by -2048 and 2047: 11 bits.
        # ie 3 bytes.
        
        SIGN_BIT = 0x10_00_00 # stick to 11 bits.
        MASK = 0x1F_FF_FF

        a &= MASK
        b &= MASK
        parity = a ^ b
        carry = ((a & b) << 1) & MASK 
        while carry:
            newparity = parity ^ carry
            newcarry = ((parity & carry) << 1) & MASK
            parity = newparity
            carry = newcarry

        # this gets the binary rep right up to bits in MASK
        # now we may need to sign extend:
        # moral: twos complement addition works without mod
        if parity & SIGN_BIT:
            parity |= ~MASK # ~ SIGN_BIT gives you the one pattern at the top.      
            # ~ SIGN_BIT would give you 
            # 11110111111
            # 11110000000


        return parity


        # why do we think this loop will end?
        # what happens to the number of set bits on carry
        # carry is bitwise and, number of ones is at most equal to min of the two operands. 

        # the left most bit of the initial carry is one beyond the largest initial operator. that bit will not be set on parity, so the max
        #number of carry bits decreases by one every step. 

        # need to think of two negatives. and one of each
        # consider -1 + 0. parity works, no carry. ok
        # consider -1 + 1. 000001 vs 111110
        # parity will be 111111
        # carry will be  000000
        # anser is 0000...
        # consider 2 + -1: 000010 , 111110
        # parity is 111100
        # carry is  000100
        # we need to get 000001

        # consider subtraction directly:
        # a - b, lets assume a > b.
        # when bits are 1 1 => 0
        # when 0 1 => borrow 1 from left, parity is 1, left is zero'd
        # when 1 0 => 1
        # when 0 0 => 0

        # what if a < b:
        # does this approach work?
        # eventually cannot borrow, somehow need to translate to 1111 patter.

        #  1 => 00001 ~1: 11110
        # -1 => 11111 ~-1: 00000
        #  2 => 00010
        # -2 => 11110
        #  3 => 00011 ~3 => 11100
        # -3 => 11101 ~3 + 1

        # -1 + 2 ans is 1.
        #  11111
        #  00010
        # 100001 

        # 1 - 2: 1
        # 00001
        # 11110
    #     11111

        # -1 -2: -3
        #  11111
        #  11110
        #  11101    

        # ~ (00001 + 1)
        # ~00010
        # 11101

        # -x = ~x + 1
        # ~x = -x - 1

        # 

        # -x - y = ~x + ~y +1 +1 

        # so, do ~x + ~y.
        
        # ~(~x + ~y + 2)

        # 0xFF_FF_FF_FF => 


        