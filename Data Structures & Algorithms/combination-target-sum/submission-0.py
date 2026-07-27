class Solution:

    def _helper(self, sorted_nums: List[int], target: int) -> List[List[int]]:
        if sorted_nums == []:
            if target == 0:
                return [[]] # there is a single empty partition
            else:
                return [] # no partition can be formed here
        
        h = sorted_nums[0]
        max_reps = target // h

        ans = []
        for i in range(max_reps+1):
            remaining = self._helper(sorted_nums[1:], target - i*h)
            ans.extend([h]*i + s for s in remaining)
        return ans

        


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## approach idea:
        ## different from standard combinations bc elements can be re-used, but we need to avoid duplicate sets.

        ## idea: assume unique input elements and sort them. 
        # for each element we must choose how many times we add it, and then move forward.
        # take the largest element h
        # if while n*h <= target:
        #   we can return [h, ] with nums[1:] and target = t - h, [h, h, ]...

        ## assume these are positive numbers otherwise you could have infinite results
        sorted_nums = sorted(set(nums))
        return self._helper(sorted_nums, target)


