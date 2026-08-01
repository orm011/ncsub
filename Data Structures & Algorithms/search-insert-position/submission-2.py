class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## better option for large arrays: binary search.
        ## locate the index of the first element >= target
        left = 0
        right = len(nums) - 1
        if target <= nums[left]:
            return left
        if target > nums[right]:
            return len(nums)

        while left + 1 < right:
            mid = (left + right) // 2 
            if target <= nums[mid]:
                right = mid
            else:
                left = mid

            # always nums[left] < target and target <= nums[right].

        # special cases
        # empty: constraints rule it out
        # single element less than target. will return 1
        # single element greater than or equal to target. will return 0
         

        return right