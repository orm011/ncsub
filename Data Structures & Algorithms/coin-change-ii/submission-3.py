class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # idea: recursive on the amount
        # for a given amount n 
        # note one set of denominitions in different order
        # only count as 1 (should note be double counted)
        
        # rough idea: recursive. k means only using coins[:k]
        # not sure how to avoid duplicates otherwise
        memoize = {}
        coins.sort()

        def dfs(amount: int, k: int):
            if k == 0: # all coins used
                return 1 if amount == 0 else 0
            elif k == 1:
                return 1 if amount % coins[k-1] == 0 else 0

            # case k == 1: will check all factors,
            # at most one will match amount            
            if (amount,k) in memoize:
                return memoize[(amount,k)]

            ways = 0
            denom = coins[k-1]
            max_factor = amount // denom
            for factor in range(max_factor + 1):
                options = dfs(amount - factor*denom, k-1)
                ways += options
            
            memoize[(amount,k)] = ways

            return ways
        

        return dfs(amount, len(coins)) # can use all coins
        # runtime: O(amount * k) cases.
        # each case possibly taking amount/denom time (loop)
        # space: similar.
        # can i do away with one