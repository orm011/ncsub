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
            return self.canSum(nums, double_target//2)

    def canSum(self, nums: List[int], target: int) -> bool:
        """returns true if a subset of nums adds up to the target"""
        # recursive property: canSum(nums, target) = canSum(nums[1:], target - nums[0]) or canSum(nums[1:], target)
        # canSum([], 0) is true, canSum([], _) is always false
        if nums == []:
            return target == 0
        if target <= 0:
            return False # all elts are non-negative. not necessary

        first = nums[0]
        return self.canSum(nums[1:], target - first) or self.canSum(nums[1:], target)
        
