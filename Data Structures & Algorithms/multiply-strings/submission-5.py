class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        a = [int(d) for d in num1[::-1]]
        b = [int(d) for d in num2[::-1]]

        n = len(a)
        m = len(b)
        out = [0] * (n + m)

        for i in range(n):
            for j in range(m):
                out[i+j] += a[i]*b[j]

        for i in range(len(out)):
            if out[i] > 9:
                carry,digit = divmod(out[i], 10)
                out[i] = str(digit)
                out[i+1] += carry
            else:
                out[i] = str(out[i])

        if out[-1] != '0':
            idx = -1
        else:
            idx = -2
        
        return ''.join(out[idx::-1])
        
