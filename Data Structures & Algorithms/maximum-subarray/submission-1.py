class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # naive approach:
        # the space of subarrays is parametrized by its start and end positions
        # exploring this space is O(N^2). There is also a sum between them, 
        # a naive loop over this space would still need to do internal sums.
        # that adds a factor of N with a naive approach.

        # insight: the partial sums can be re-used somehow.
        # by doing cumulative sum, the test for computation can be done in O(1)
        # for each of the points in the space. This shaves off a factor.
        
        cumsum = [-1 for i in range(len(nums) + 1)]
        cumsum[0] = 0
        for i in range(len(nums)):
            cumsum[i+1] = nums[i] + cumsum[i]
        
        # or lets think left to right.
        # we track the best subarray seen so far. 
        # and we track the best subarray in progress.
        best_so_far = nums[0]
        best_in_progress = nums[0]
        for i in range(1,len(nums)):
            # at each step, the best in progress can extend to the right
            # it can shrink the left side to the right as well 
            # it can become the best so far (whtout ending it)
            # note any negative strict prefix to the best so far should be removed
            next_val = nums[i]
            
            if best_in_progress <= 0:
                best_in_progress = next_val
            else:
                best_in_progress += next_val

            if best_in_progress > best_so_far:
                best_so_far = best_in_progress

            # at end of step i: best so far is the best seen :i

        return best_so_far
            

