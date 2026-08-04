class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        bests = [-1 for _ in range(amount + 1)]
        amount_stack = [amount]
        # instead of choosing the subproblem based on array,
        bests[0] = 0 # zero coins suffice for this.
        if amount == 0:
            return 0

        coins.sort()
        # only evaluate subproblems needed for the final result.
        # cannot recurse because of call stack limits.
        # but can do this with a stack 

        # big lesson here: step back to consider different parametrizations
        # my initial instinct was that iterating over the amount would be too much, 
        # and that we needed the coins array in the parametrization.
        # but if i had produced a complexity, i would have seen the n* A ^2 is bad
        if amount % coins[-1] == 0:
            return amount // coins[-1]
        counter = 0
        while amount_stack:
            # print(f"{amount_stack=}")
            amt = amount_stack[-1]
            best = float('inf')
            
            to_append = []
            for coin in coins:
                if amt - coin < 0:
                    continue
                if bests[amt - coin] == -1:   
                    to_append.append(amt - coin)
                else:
                    best = min(best, 1 + bests[amt - coin])

            if best == 1 or len(to_append) == 0:
                bests[amt] = best
                amount_stack.pop()
            else: # need dependencies
                amount_stack.extend(to_append)


        return -1 if bests[amount] == float('inf') else bests[amount]