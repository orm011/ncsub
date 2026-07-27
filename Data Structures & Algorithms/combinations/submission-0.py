class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # recursive definition:
        ## n C k = (n - 1 C k -1) + (n-1 C k) #
        if k == 0:
            return [[]]
        elif k == n:
            return [list(range(1,n+1))]
        else:
            pass

        without_n = self.combine(n-1, k)
        with_n = [s + [n] for s in self.combine(n-1, k-1)]
        return with_n + without_n



