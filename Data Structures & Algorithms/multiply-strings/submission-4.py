class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        l = m + n

        output = [0 for _ in range(n+m)]
        for i in range(n):
            for j in range(m):
                powi = n - 1 - i # 0 -> n - 1 n-1 -> 0
                powj = m - 1 - j # 0 -> m - 1

                oidx = l - 1 - powi - powj
                # eg 0 pow for both goes to pos l -1 (last)
                # n - 1 + m - 1 pow goes to l -1  (- m + 1 - n_ + 1= 0
                output[oidx] += int(num1[i])*int(num2[j])
                
        mostsig = -1
        for i in range(-1, -l, -1):
            carry,digit = divmod(output[i], 10)
            output[i-1] += carry
            output[i] = str(digit)
            if carry:
                mostsig = i-1
            elif digit:
                mostsig = i

        output[0] = str(output[0])
            
        return ''.join(output[mostsig:])

        

          