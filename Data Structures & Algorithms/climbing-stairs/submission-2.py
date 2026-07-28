class Solution:
    def climbStairs(self, n: int) -> int:
        # if n > 0 can always take one step. then climb n-1 stairs.
        # if n >1 , geq than two remain, can take two steps, then climb n-2 stairs
        # recursive n = 0: 1 way. n = 1. 1 way. n = 2. 2 ways.
        # n = 3. start with one: then have two ways. start with two: then have one way. total 3.
        soln = [-1 for i in range(max(n+1,2))]
        soln[0] = 1
        soln[1] = 1

        for i in range(2,len(soln)):
            soln[i] = soln[i-1] + soln[i-2]

        return soln[n]     
        