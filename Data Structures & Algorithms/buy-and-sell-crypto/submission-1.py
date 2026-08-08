class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea, if we simply track min and max,
        # and max happens after min, then that is the solution.
        # however, that may not work well, we need to find
        # i,j so that we maxi<j  price[j] - price[i]
        # brute force would be taking all pairs i < j
        # this is O(n^2)
        # 
        # Lets try for a O(n) one.
        # for each i there is a max j after.
        # that max can be re-used for multiple i, until we pass that j.
        # also, that worse max only makes sense if there is a lower min ahead.


        min_idx = 0
        max_idx = 0
        best_diff = 0

        current_min_idx = 0

        # invariant: best_diff only goes up.
        # did it ever see 7
        for i in range(1, len(prices)):
            #print(f"{i=} {best_diff=} {min_idx=} {max_idx=} {current_min_idx=}")
            assert max_idx >= min_idx
            # invariant: max_idx >= min_idx
            # idea. lets go over each value, it will either improve the max.
            # or it will propose a new min, which could work out better.
            curr_diff = prices[i] - prices[current_min_idx]
            if  curr_diff >= best_diff:
                min_idx = current_min_idx # can stay the same.
                max_idx = i
                best_diff = curr_diff

            if prices[i] < prices[current_min_idx]:
                # better potential starting point found
                current_min_idx = i

            # why this is correct?
            # consider the best option in the array.
            # it is easy to see it satisfies the first condition.
            # if something satisfies the first condition in the array before it
            # and nothing better comes up after, then it must be the best.
        return prices[max_idx] - prices[min_idx] # 0 alrady included.


        