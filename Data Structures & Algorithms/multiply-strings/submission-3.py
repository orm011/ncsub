class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # basic idea: every digit of num1 with every digit of num2, 
        # tracking powers of 10. 
        # final result: each position with power 10^k
        # is sum of a_i*b_{k-i}*10^i*10^(k - i)
        # ie, pick k. then iterate over all i: 
        # a_0 b_k, a_1 b_{k-1} , a_2 b_{k-2} .. a_k b_{0}
        n = len(num1)
        m = len(num2)

        output = [0 for _ in range(n+m)]
        mostsig = -1
        for pos in range(-1, -n-m, -1): # pos -n-m is only used for carry
            #print(f'{pos=} {output=}')
            # getting the indices correct: 
            # pos: -k in the output array corresponds 
            # to power of -1 -> 0, -2 -> 1 , -n - m -> n + m - 1
            # - n - m 
            # output[-1], output[-2]
            k = - pos - 1 # k is power of 10.
            
            i = 0 # idx2 = - k + i - 1.
            # hence idx2 < -len(num2) iff 
            # -k + i -1 < -len(num2)
            # i < -len(num2) + k + 1
            # hence start i at 
            i = max(k - len(num2) + 1,0)
            #i = 0 
            while True:
                if i > k:
                    break
                idx1 = -i - 1  # 0 -> -1, 1-> -2  
                idx2 = -(k - i) - 1 

                if idx1 < -len(num1): # no more digits
                    d1 = 0
                else:
                    d1 = int(num1[idx1]) 

                d2 = int(num2[idx2]) if idx2 >= -len(num2) else 0
                output[pos] += d2*d1
                i+=1

            carry, digit = divmod(output[pos], 10)
            output[pos] = str(digit) # there may be a carry
            if carry:
                mostsig = pos - 1
            elif digit:
                mostsig = pos

            if pos-1 >= -len(output):
                output[pos-1] = carry
            else:
                assert carry == 0
            
        output[0] = str(output[0]) # last carry
        # start from mostsig inclusive. will be -1 in worst case 
        return ''.join(output[mostsig:])

        





