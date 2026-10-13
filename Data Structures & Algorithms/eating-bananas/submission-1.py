import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # want 
        # argmin k \sum_i ceil(piles[i]/k) <= h
        # argmin k \sum_i k * ceil(piles[i]/k) <= k*h
        # piles[i] + k - 1 >= k * ceil(piles[i]/k) >= piles[i]

        # if i wanted to compute for a given k, how long it takes
        # to eat all piles, i would:
        
        
        n = len(piles)


        # one approach: go  down from seomthing that works.\

        # math.ceil(sum piles[i])/h <= best k <= max(piles[i])


        # piles[i] + k - 1 >= k * ceil(piles[i]/k) >= piles[i]
        # if \sum piles[i] + n*(k-1) <= k*h then we know k is valid, but not necessarily minimum.
            # \sum piles[i] <= h*k - n*k + n
            # (\sum piles[i] - n ) / (h - n) <= k <= max_i (piles[i])

        # idea: "binary search"
        # check: we can compute time for that k.
        # if it works, and k - 1 does not. found it.
        # if it does not work, then try (k + k_0) //2
        # if both k and k-1 work, upper = k-1.
        # lower 0

        def check(k) -> bool:
            if k == 0:
                return False
            
            hours = 0
            for i in range(n):
                hours += math.ceil(piles[i]/k)
            return hours <= h

        assert n <= h
        sumpile = sum(piles)


        lower, upper = min(math.ceil(sumpile/h), max(piles)), max(piles)
        while lower <= upper:
            k = (lower + upper + 1)//2 # cannot equal lower.
            
            kok = check(k)
            km1ok = check(k-1)

            if kok and not km1ok: # found it
                return k
            elif kok and km1ok:
                upper = k - 1
            elif not kok and not km1ok:
                lower = k + 1

        
        # invariant: 
        # upper - lower always decreases. now yes. 
        # check(upper) is always true.
        # check(lower-1) is always false.
        # does loop always end: yes.   
        # if upper == lower, then kok and not km1ok, so we will return.

        # runtime: n * log_2 (max(piles))

        # example: [2] h = 2. ans is k = 1. ok
        # example: [2] h = 1. ans ok
        # example: [1,2] h = 2. ans: k = 2
        # example [1,2] h = 3. ans: k = 1

        