from collections import defaultdict
import math

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ## for a given target, and non empty nums (:n+1)
        ## the problem dp(n, target) = dp(n-1, target + nums[n-1]) + dp(n-1, target - nums[n-1]) 
        ## ie, the last number can be used exactly two ways, each determines a partition of solutions.
        ## note wwe cannot reuse the number we already used.
        ## if the number is 0, technically both are the same way but lets not worry.

        # this gives us a recursion space over two d: the nums position and the target total.
        # targets can range from -1000, 1000 as inputs, but can potentially fall outside this window in the recursion
        memoized = defaultdict(lambda : -1)
        
        # options to speed up: 
        # can we parametrize differently.  fewer subproblems.
        # eg. only by k, or only by target.
        # we know n is bound to 20 there are only 2*20, ie a million possible sums.
        # we know some sums are out of bound
        # lets track max sums and min sums at each n:
        nums = sorted([abs(n) for n in nums]) # sort to make the bounds as tight as possible
        target = abs(target)
        max_sums = [0 for _ in nums]
        max_sums[0] = nums[0]
        
        gcds = [0 for _ in nums]
        gcds[0] = nums[0] # could be 0 though

        # can i get a min sum somehow..., min non zero sum also.
        # min_sum[0] # is that element.
        # min_sum[1] # could be 0 if equal, or abs( 1 - 0)
        # min_sum[2] # 

        for i in range(1,len(nums)):
            num = nums[i]
            max_sums[i] = max_sums[i-1] + num
            gcds[i] = math.gcd(gcds[i-1], num)

        def dp(k: int, target: int) -> int: # solution for nums[:k]
            num = nums[k]
            if target == 0 and num == 0: # short circuit for only 0
                ans = 1 << (k+1) # for k = 0, two ways.
            elif k == 0: # nums is at least length 1
                return 1 if num == target else 0
            elif target > max_sums[k]:
                ans = 0
            elif target != 0 and target < gcds[k]:
                ans = 0
            elif gcds[k] > 0 and target % gcds[k] != 0: # remaining cannot add to this
                ans = 0
            else:
                ans = memoized[(k,target)]
                if ans != -1:
                    return ans
                neg_sign = dp(k-1, target + num)
                pos_sign = dp(k-1, abs(target - num)) # symmetry around sign of target
                ans = neg_sign + pos_sign
                memoized[(k,target)] = ans

            return ans
            

        ans = dp(n-1, target)
        #print(f"{len(memoized)=} {memoized=}")
        return ans
        # analysis: at most once per case, len(nums) *  # number of possible targets args. (can be sum(nums) big)
        # similar with space.

        ## identified some symmetry on the target, reducing cases.


        

