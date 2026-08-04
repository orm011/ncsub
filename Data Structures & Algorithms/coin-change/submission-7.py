class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        bests = [-1 for _ in range(amount + 1)]
        amount_stack = [amount]
        # instead of choosing the subproblem based on array,
        bests[0] = 0 # zero coins suffice for this.
        if amount == 0:
            return 0
        # only evaluate subproblems needed for the final result.
        # cannot recurse because of call stack limits.
        # but can do this with a stack 

        # big lesson here: step back to consider different parametrizations
        # my initial instinct was that iterating over the amount would be too much, 
        # and that we needed the coins array in the parametrization.
        # but if i had produced a complexity, i would have seen the n* A ^2 is bad
        while amount_stack:
            amt = amount_stack[-1]
            missing_deps = False
            best = float('inf')
            for coin in coins:
                if amt - coin < 0:
                    continue

                if bests[amt - coin] == -1:   
                    amount_stack.append(amt - coin)
                    missing_deps = True
                else:
                    best = min(best, 1 + bests[amt - coin])

            if not missing_deps:
                bests[amt] = best
                amount_stack.pop()

        return -1 if bests[amount] == float('inf') else bests[amount]