class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} # parametrized on amount only
        # instead of choosing the subproblem based on array,
        bests = [-1 for _ in range(amount + 1)]
        bests[0] = 0 # zero coins suffice for this.
        # best[am] holds answer for amount am. 
        for amt in range(1, amount + 1):
            best = float('inf')
            for coin in coins:
                if amt - coin < 0:
                    continue
                best = min(best, 1 + bests[amt - coin])

            bests[amt] = best  

        return -1 if bests[amount] == float('inf') else bests[amount]