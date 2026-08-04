class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        solutions = {} # maps (position in coins, amount) -> optimal or -1
        def optimalCoinChange(coins: List[int], amount: int) -> int:
            # the subproblems are parametrized by the position in coins, and the amount.
            # the amount values are not neatly foreseeable at the start (though range from 0 to amount)
            # so lets use recursion to do lazy evaluation of only the cases that matter

            if coins == []:
                if amount == 0:
                    return 0
                else:
                    return -1
            else:
                memoization_key = (len(coins),  amount) 
                if memoization_key in solutions:
                    return solutions[memoization_key]
                
                last = coins[-1]
                options = []
                for factor in range(0, (amount // last) + 1):
                    opt = optimalCoinChange(coins[:-1], amount - factor*last)
                    if opt != -1:
                        options.append(opt + factor)
                
                if options == []:
                    ans =  -1
                else:
                    ans = min(options)
                
                solutions[memoization_key] = ans
                return ans

        return optimalCoinChange(coins, amount)