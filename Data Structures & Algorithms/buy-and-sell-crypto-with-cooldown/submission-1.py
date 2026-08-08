class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # constraint: if sell in i, then must skip i+1.
        # without the constraint
        # we can split the array into monotonic increasing subseqs and
        # that will be the optimal solution

        # the optimal profit for the price array at time t+1
        # could either be the same as solution for time t (no trades happen at t+1)
        # or it could involve t+1 somehow (only selling is possible at that point),
        # but that would require a buy happening at the minimum price out of 
        # two days more beyond the last sell.
        
        # hence sol(t+1) = max_i=1...t-3(sol(i) + best_trade(i+2,t+1))
        # computing best trade for all those problems, how hard is it?
        # best_trade(i+2, t+1) must end at t+1 (otherwise already included in sol(t))
        # hence best_trade only requires the min_i+2...t+1 price
        # we only need to track the min from the last trade

        profit_max = [-1 for _ in prices] 
        # position i is the optimal total profit for the problem restricted to prices[:i+1], ie including i. 
        # answer is profit_max[-1]

        sell_events = [-1 for _ in prices] 
        # will be 1 at pos i if the best solution
        # sells at pos i.
        arg_min = [-1 for _ in prices] # position of min since last event.

        profit_max[0] = 0 # 
        sell_events[0] = 0 # no restrictin on buying next
        arg_min[0] = 0 
        # meant to track the arg min price since the last sell event.
        # needs to be a legal move, ie, cannot happen until +2 from sell event.

        # current mistake: we should consider trades that end in t+1, but
        # start at any point 

        for i in range(1, len(prices)):
            best_so_far = 0      
            for j in range(i):
                sell_now = prices[i] - prices[j]            
                if j - 2 >= 0:
                    past_profit = profit_max[j-2]
                else:
                    past_profit = 0

                total_profit = sell_now + past_profit
                if total_profit > best_so_far:
                    best_so_far = total_profit
    
            #print(f"{profit_max=} {best_so_far=}")

            if best_so_far > profit_max[i-1]:
                profit_max[i] = best_so_far
            else:
                profit_max[i] = profit_max[i-1]
                

        return profit_max[-1]

        