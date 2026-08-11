class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # assume offset 0 right now. 
        # for the journey to be possible,
        # let sum_gas[i] be the partial sum of gas starting at 0 and inclding i.
        # let sum_cost[i] be the partial sum of cost starting at 0.
        # can reach reach i+1 if and only if
        # sum_gas[i] >= sum_cost[i] for all i 
        # some offsets may be poor starting points bc the chain is
        # broken somewhere along the way

        # they say they guarantee at most one solution
        # intuitively want to start at a place where sum_gas increases
        # quickly, before sum_cost increases
        # consider the array diff[i] = gas[i] - cost[i]
        # sum_diff[i] = sum starting at some offset
        # no matter where the offset starts, the point before will have
        # the full difference after a cycle, which must be greater than 0 (since it must be possible to travel, so the amount of total fuel must exceed total fuel needed)
        sum_diff = [0 for _ in gas]
        min_idx = 0
        for i in range(len(gas)):
            sum_diff[i] += gas[i] - cost[i] + sum_diff[i-1 % len(gas)]
            if sum_diff[i] < sum_diff[min_idx]:
                min_idx = i

        #print(f"{sum_diff=}")
        if sum_diff[-1] < 0:
            return -1
    
        if sum_diff[min_idx] >= 0:
            return 0

        best_idx = (min_idx + 1) % len(gas)
        # the new diffs are the same as before but subtracting 
        #print(f"{min_idx=}{best_idx=}")
        diff_offset = sum_diff[min_idx]
        return best_idx
        # for i in range(len(gas)):
        #     idx = (best_idx + i) % len(gas)
        #     sum_diff[idx] = gas[idx] - cost[idx] 
        #     if i > 0:
        #         sum_diff[idx] += sum_diff[(idx - 1) % len(gas)]

        #     #print(f"{i=} {idx=} {sum_diff=}")
        #     if sum_diff[idx] < 0:
        #         return -1
        
        # not sure my guess of optimality is true
        # whats the argument here. 
        # if everything passes, then that's a solution.
        # if something does not pass, then we need to show
        # it means it cannot possibly. 
        # return best_idx
        



        




        