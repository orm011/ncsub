class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ## option1: more general problem. canPartitionK: can we partition to achieve difference k.
        ## then we can check where we want the first element to go. Note it must go somewhere.
        ## observation2: we know sum(set). so, problem is equivalent to finding subset adding up to S/2.
        ## for element k, if elt is in subset, then the remainer must be S/2 - k. can we sum to that?

        double_target = sum(nums)
        if double_target % 2 == 1:
            return False
        else:
            previous = {}
            return self.canSum(previous, nums, double_target//2)

    def canSum(self, previous: dict[(int,int), int], nums: list[int], target: int) -> bool:
        """returns true if a subset of nums adds up to the target"""
        # recursive property: canSum(nums, target) = canSum(nums[1:], target - nums[0]) or canSum(nums[1:], target)
        # canSum([], 0) is true, canSum([], _) is always false
        if nums == []:
            return target == 0
        elif target <= 0:
            return False # all elts are non-negative. not necessary
        elif len(nums) == 1:
            return target == nums[0]
        else:
            pass

        soln = previous.get((len(nums), target))
        if soln is not None:
            return soln
        
        first = nums[0]
        ans =  self.canSum(previous, nums[1:], target - first) or self.canSum(previous, nums[1:], target)
        previous[(len(nums), target)] = ans
        return ans

    def canSumBottomUp(self, nums: List[int], target: int) -> bool:
        # difficulty:   different possible targets that will come up as we traverse this
        # recursion is hard to know in advance. 
        # this makes it difficult to build the solution bottom up
        # alternative: dictionary
        pass

        
