class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """iterative version"""
        optimal = [-1 for i in range(len(cost) + 1)]
        # optimal[i] is the best cost from starting at cost[i-1]
        if len(cost) == 0:
            return 0
        elif len(cost) == 1:
            return cost[0]
        
        cost.reverse()

        optimal[0] = 0
        optimal[1] = cost[0]

        for pos in range(2,len(cost)+1):
            best = min(optimal[pos-1], optimal[pos-2])
            optimal[pos] = cost[pos-1] + best

        return min(optimal[len(cost)], optimal[len(cost) - 1])