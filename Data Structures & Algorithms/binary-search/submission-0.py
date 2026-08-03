class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        low = 0
        high = len(nums) - 1

        # invariant low <= high
        # invariant: nums[low] < target <= high
        # when low == high, check for equality.
        if target < nums[low] or target > nums[high]:
            return -1

        if target == nums[0]:
            return 0
        
        # second invariant is true now at the start.
        while low + 1 < high:
            midpoint = low + (high - low)//2
            if target <= nums[midpoint]:
                high = midpoint
            else:
                low = midpoint

        return high if nums[high] == target else -1
